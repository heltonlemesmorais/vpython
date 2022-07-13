from vpython import*
# reenderização
scene = canvas(height=600)
graph(height=800)


partes_fog = []
height = 0.5

# corpo cilindrico do foguete
partes_fog.append(cylinder(pos=vec(0, 1, 0), color=color.red, size=vec(
    height, 0.1, 0.1), axis=vec(0, 1, 0), make_trail=True))

# bico do foguete
partes_fog.append(cone(pos=partes_fog[0].pos+partes_fog[0].size.x*partes_fog[0].axis*2, color=color.white, size=vec(
    partes_fog[0].size.y, partes_fog[0].size.y, partes_fog[0].size.y), axis=vec(0, 1, 0)))

# caudas do foguete
partes_fog.append(triangle(v0=vertex(pos=partes_fog[0].pos+0.5*partes_fog[0].size.y*vec(1, 0, 0), color=color.red), v1=vertex(
    pos=partes_fog[0].pos+1.5*partes_fog[0].size.y*vec(1, 0, 0), color=color.red), v2=vertex(pos=partes_fog[0].pos+0.5*partes_fog[0].size.y*vec(1, 2, 0), color=color.red)))

partes_fog.append(triangle(v0=vertex(pos=partes_fog[0].pos+0.5*partes_fog[0].size.y*vec(-1, 0, 0), color=color.red), v1=vertex(
    pos=partes_fog[0].pos+1.5*partes_fog[0].size.y*vec(-1, 0, 0), color=color.red), v2=vertex(pos=partes_fog[0].pos+0.5*partes_fog[0].size.y*vec(-1, 2, 0), color=color.red)))

partes_fog.append(triangle(v0=vertex(pos=partes_fog[0].pos+0.5*partes_fog[0].size.y*vec(0, 0, 1), color=color.red), v1=vertex(
    pos=partes_fog[0].pos+1.5*partes_fog[0].size.y*vec(0, 0, 1), color=color.red), v2=vertex(pos=partes_fog[0].pos+0.5*partes_fog[0].size.y*vec(0, 2, 1), color=color.red)))

partes_fog.append(triangle(v0=vertex(pos=partes_fog[0].pos+0.5*partes_fog[0].size.y*vec(0, 0, -1), color=color.red), v1=vertex(
    pos=partes_fog[0].pos+1.5*partes_fog[0].size.y*vec(0, 0, -1), color=color.red), v2=vertex(pos=partes_fog[0].pos+0.5*partes_fog[0].size.y*vec(0, 2, -1), color=color.red)))

# montagem foguete
fog = compound(partes_fog, pos=vec(0, 1, 0))
fog.velocity = vec(0, 0, 0)
fog.angle = 0  # angulo inicial


theta = 45*(pi/180)  # angulo lançamento
fog.v = vec(20*cos(theta), 20*sin(theta), 0)  # velocidade e trajeto
g = vec(0, -9.81, 0)  # vetor gravidade
t = 0  # tempo inicial
dt = 0.0005  # diferença tempo para reenderização da proxima posição foguete

scene.camera.follow(fog)  # define foguete como ponto central da camera

# solo lançamento
solo = box(pos=vec(20, -0.2, 0), size=vec(60, 0.1, 10), texture=textures.rock)


# vetor x velocidade
fog.ex = vec(5*cos(theta), 0, 0)
attach_arrow(fog, "ex", color=color.blue, shaftwidth=0.05)

# vetor y força velocidade-gravidade
fog.ey = vec(0, 20*sin(theta), 0)
attach_arrow(fog, "ey", color=color.green, shaftwidth=0.05)


# rotação do foguete conforme trajeto
angle_amplitude = pi
angle_period = 20
angle = fog.angle

attach_trail(fog, radius=0.001)  # trajeto foguete

# looping para atualização do foguete a cada instante
while fog.pos.y >= 0.01:
    rate(300)

    fog.v = fog.v + g*dt
    fog.ey = fog.ey + g*dt
    fog.pos = fog.pos + fog.v*dt

# equação que define angulo de posição foguete conforme trajeto
    new_angle = angle_amplitude*sin(-2*pi*t/angle_period)
    fog.rotate(angle=new_angle-fog.angle, axis=vec(0, 0, 1))
    fog.angle = new_angle

    legenda1 = label(pos=vec(
        fog.pos.x-1, fog.pos.y+1, 0), text="legenda")
    legenda2 = label(pos=vec(
        fog.pos.x+1, fog.pos.y-1, 0), text="legenda")

    legenda1.text = "altura= {:0.2f}".format(fog.pos.y)
    legenda2.text = "distancia= {:0.2f}".format(fog.pos.x)
    rate(300)
    legenda1.visible = False
    legenda2.visible = False

    t = t + dt
