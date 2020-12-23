from math import sqrt

print("== [물체 이동 거리 계산기] ==")
print("물체의 높이와 속도를 입력받아 이동 거리를 계산하는 프로그램입니다.")
print("중력 가속도는 9.8m/s로 가정합니다.")

height = input("물체를 던질 높이를 설정해주세요. : ")
print("Object height : {}m".format(height))
height = int(height)

accel = input("물체를 던질 속력을 입력해주세요. : ")
print("Object Acceleration : {}m/s".format(accel))
accel = int(accel)

time = sqrt((2 * height) / 9.8)
dist = accel * time

print("소요 시간 : {}초".format(time))
print("수평 방향 이동 거리 : {}m".format(dist))
print("==============================")