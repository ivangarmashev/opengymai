from time import sleep

import gym
env = gym.make('SpaceInvaders-v0')
env.reset()
env.render()
action = env.action_space.sample()
new_state, reward, is_done, info = env.step(action)
print(is_done, info)
env.render()
is_done = False
while not is_done:
    action = env.action_space.sample()
    new_state, reward, is_done, info = env.step(action)
    # print(info)
    sleep(0.1)
    env.render()

input('123')
