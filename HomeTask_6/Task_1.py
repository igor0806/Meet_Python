from time import sleep

traffic_light_a = ["Red", "Yellow", "Green"]
traffic_light_p = ["Red", "Green"]
while True:
    for _ in range(4):
        print(f'{traffic_light_a[0]:<10} {traffic_light_p[1]}')
        sleep(1)

    for _ in range(2):
        print(f'{traffic_light_a[1]:<10} {traffic_light_p[1]}')
        sleep(1)

    traffic_light_a = traffic_light_a[::-1]
    traffic_light_p = traffic_light_p[::-1]

