from matplotlib import pyplot as plt
import math

#2つの値の間の等間隔な浮動小数点数の生成
def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start += increment
    return numbers

#投射運動物体の軌跡を描く
def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')

def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8
    #飛行時間の計算
    t_flight = 2*u*math.sin(theta)/g
    #グラフの描写間隔の決定
    intervals = frange(0, t_flight, 0.001)
    #x,yの距離を入れるリストを作成
    x = []
    y = []
    for t in intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*g*t*t)
    draw_graph(x, y)

if __name__ == '__main__':
    try:
        u = float(input('Enter the initial velocity (m/s): '))
        theta = float(input('Enter the angle of projection (degrees): '))
    except ValueError:
        print('You entered an invalid input')
    else:
        draw_trajectory(u, theta)
        plt.show()
