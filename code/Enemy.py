#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, WIN_HEIGHT
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.up = True
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        if self.name == 'Enemy3':
            if self.up:
                self.rect.centery -= (ENTITY_SPEED[self.name])
                self.rect.centerx -= (ENTITY_SPEED[self.name])
            if not self.up:
                self.rect.centery += (ENTITY_SPEED[self.name] * 2)
                self.rect.centerx -= (ENTITY_SPEED[self.name] * 2)
            if self.rect.top <= 0:
                self.up = False
            if self.rect.bottom >= WIN_HEIGHT:
                self.up = True

        else:
            self.rect.centerx -= (ENTITY_SPEED[self.name])

    def move_enemy(self, up_or_down: int):
        self.rect.centery -= (ENTITY_SPEED[self.name] * up_or_down)

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))
