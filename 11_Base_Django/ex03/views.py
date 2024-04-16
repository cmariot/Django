from django.shortcuts import render


# Create your views here.
def index(request):

    class Color:
        def __init__(self, name, rgb):
            self.name = name
            self.rgb = list(rgb)
            self.coef = [(255 - channel) / 255 for channel in self.rgb]
            self.gap = 0

        def __str__(self):
            return ", ".join([str(channel) for channel in self.rgb])

        def change_color(self):
            for i in range(3):
                self.rgb[i] += self.gap * self.coef[i]
                self.rgb[i] = min(255, max(0, self.rgb[i]))
            if self.gap == 0:
                self.gap = 255 / 50
            return str(self)

    context = {
        "colors": {
            "Black": Color("Black", (0, 0, 0)),
            "Red": Color("Red", (255, 0, 0)),
            "Green": Color("Green", (0, 255, 0)),
            "Blue": Color("Blue", (0, 0, 255)),
        },
        "max_lines": range(50),
    }
    return render(request, "ex03/templates/index.html", context)
