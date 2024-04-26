from .forms.create_tips import CreateTipForm
from django.http import HttpResponseRedirect
from .models import Tip
from django.shortcuts import render
from user.models import User
from user.decorators import is_logged_in


def _has_voted(tip_users, username):
    """
    Return True if the user has voted on the tip, False otherwise.
    The user has voted if he is in the list of users who have voted.
    """
    vote = False
    for tip_user in tip_users:
        if tip_user.username == username:
            vote = True
            break
    return vote


def _get_tips(user: User):

    """
    Return a list of tips stored in a dictionary.
    This list will be used in the templates
    """

    if not Tip.objects.exists():
        return []

    tips = Tip.objects.all()
    if not tips:
        return []

    tips = sorted(
        tips,
        key=lambda tip: (tip.created_at),
        reverse=True,
    )

    username = user.username

    tips_list = []
    for tip in tips:

        nb_up = tip.up.count()
        nb_down = tip.down.count()
        has_upvoted = _has_voted(tip.up.all(), username)
        has_downvoted = _has_voted(tip.down.all(), username)

        tips_list.append(
            {
                "id": tip.id,
                "author": tip.author.username,
                "content": tip.content,
                "created_at": tip.created_at.strftime("%B %d, %Y at %H:%M:%S"),
                "nb_up": nb_up,
                "nb_down": nb_down,
                "has_upvoted": has_upvoted,
                "has_downvoted": has_downvoted,
                "user_can_delete": user.can_delete_tip(tip),
                "user_can_downvote": user.can_downvote(tip),
            }
        )
    return tips_list


@is_logged_in
def post_tip(request):

    """
    This view is used to create a tip.
    If the form is valid, the tip will be saved in the database
    """

    if not request.user.is_authenticated:
        return HttpResponseRedirect("login")

    if request.method == "POST":
        form = CreateTipForm(request.POST)
        try:
            if form.is_valid():
                user = request.user
                form.save(user)
                return HttpResponseRedirect("/")
        except Exception as e:
            form.add_error("content", str(e))

        context = {
            "username": request.user.username,
            "is_logged_in": True,
            "create_tip_form": form,
            "tips_list": _get_tips(request.user),
            "reputation": request.user.reputation,
        }
        return render(request, "homepage/templates/index.html", context)
    else:
        return HttpResponseRedirect("/", {"error": "Page not found"})


@is_logged_in
def remove_tip(request, tip_id):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponseRedirect("login")
        try:
            tip = Tip.objects.get(id=tip_id)
            if request.user.can_delete_tip(tip):
                nb_up = tip.up.count()
                nb_down = tip.down.count()
                tip.author.lose_reputation(nb_up * 5 - nb_down * 2)
                tip.delete()
                return HttpResponseRedirect("/")
            return HttpResponseRedirect("/")
        except Tip.DoesNotExist:
            return HttpResponseRedirect("/")


@is_logged_in
def upvote_tip(request, tip_id):

    """
    An upvote will add 5 points of reputation to the author of the Tip.

    - If the user has already upvoted the Tip, the upvote will be removed.
    - The user can upvote his own Tip, and the reputation will be added to his
      account.
    - If the user has downvoted the Tip, the downvote will be removed and the
      author will gain 2 points of reputation.

    """

    if request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponseRedirect("login")
        try:

            tip = Tip.objects.get(id=tip_id)
            tip_author = tip.author

            if request.user in tip.up.all():
                # Remove an upvote -> -5 reputation
                tip.up.remove(request.user)
                tip.save()
                tip_author.lose_reputation(5)

            else:
                # Add upvote -> +5 reputation
                tip.up.add(request.user)
                tip.save()
                tip_author.gain_reputation(5)

                if request.user in tip.down.all():
                    # Remove downvote if it exists -> +2 reputation
                    tip.down.remove(request.user)
                    tip.save()
                    tip_author.gain_reputation(2)

            return HttpResponseRedirect("/")
        except Tip.DoesNotExist:
            return HttpResponseRedirect("/")
        except User.DoesNotExist:
            return HttpResponseRedirect("/")


# un downvote enlèvera 2 points de réputation à l’auteur du Tip
@is_logged_in
def downvote_tip(request, tip_id):
    if request.method == "POST":
        if not request.user.is_authenticated:
            return HttpResponseRedirect("login")
        try:

            tip = Tip.objects.get(id=tip_id)
            tip_author = tip.author

            if not request.user.can_downvote(tip):
                error = "You need at least 15 reputation to downvote that tip."
                return HttpResponseRedirect("/", {"error": error})

            if request.user in tip.down.all():
                # Remove downvote -> +2 reputation
                tip.down.remove(request.user)
                tip.save()
                tip_author.gain_reputation(2)

            else:
                # Add downvote -> -2 reputation
                tip.down.add(request.user)
                tip.save()
                tip_author.lose_reputation(2)

                if request.user in tip.up.all():
                    # Remove upvote if it exists -> -5 reputation
                    tip.up.remove(request.user)
                    tip.save()
                    tip_author.lose_reputation(5)
            return HttpResponseRedirect("/")
        except Tip.DoesNotExist:
            return HttpResponseRedirect("/")
