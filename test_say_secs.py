# saysecs (pyStage, converted from Scratch 3)

from pystage.en import Sprite, Stage

stage = Stage()
stage.add_backdrop('backdrop1')
stage.create_variable('my variable')
sprite1 = stage.add_a_sprite(None)
sprite1.set_name("Sprite1")
sprite1.set_x(217)
sprite1.set_y(-134)
sprite1.go_to_back_layer()
sprite1.go_forward(1)
sprite1.add_costume('costume1', center_x=48, center_y=50)
sprite1.add_costume('costume2', center_x=46, center_y=53)


def when_program_starts_1(self):
    self.say_for_seconds("for score and seven years ago victo norman  tried to teach  CS 112 and gto bored at his desk and was sleeping on the job, jk!", 2.0)

sprite1.when_program_starts(when_program_starts_1)

stage.play()