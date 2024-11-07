from arestour import AresTour

arestour = AresTour()

while arestour.running != 0:
    arestour.event_handler()
    arestour.draw()
