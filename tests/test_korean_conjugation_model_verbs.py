# -*- coding: utf-8 -*-

from korean_conjugator import *

def check(func, infinitive, expected):
    result = func(infinitive)
    message = (u'%s("%s") != "%s" (returned "%s")' % (func.__name__, infinitive, expected, result)).encode('utf-8')
    result = result.replace(' ', '').replace('?', '')
    assert result == expected, message

def test_model_verbs():
    yield check, declarative_present_informal_low, u'기다', u'겨'
    yield check, declarative_past_informal_low, u'기다', u'겼어'
    yield check, declarative_future_informal_low, u'기다', u'길거야'
    yield check, inquisitive_present_informal_low, u'기다', u'겨'
    yield check, inquisitive_past_informal_low, u'기다', u'겼어'
    yield check, propositive_present_informal_low, u'기다', u'겨'
    yield check, declarative_present_informal_high, u'기다', u'겨요'
    yield check, declarative_past_informal_high, u'기다', u'겼어요'
    yield check, declarative_present_informal_low, u'기다', u'겨'
    yield check, declarative_past_informal_low, u'기다', u'겼어'
    yield check, declarative_future_informal_low, u'기다', u'길거야'
    yield check, inquisitive_present_informal_low, u'기다', u'겨'
    yield check, inquisitive_past_informal_low, u'기다', u'겼어'
    yield check, propositive_present_informal_low, u'기다', u'겨'
    yield check, declarative_present_informal_high, u'기다', u'겨요'
    yield check, declarative_past_informal_high, u'기다', u'겼어요'
    yield check, declarative_present_informal_low, u'지다', u'져'
    yield check, declarative_past_informal_low, u'지다', u'졌어'
    yield check, declarative_future_informal_low, u'지다', u'질거야'
    yield check, inquisitive_present_informal_low, u'지다', u'져'
    yield check, inquisitive_past_informal_low, u'지다', u'졌어'
    yield check, propositive_present_informal_low, u'지다', u'져'
    yield check, declarative_present_informal_high, u'지다', u'져요'
    yield check, declarative_past_informal_high, u'지다', u'졌어요'
    yield check, declarative_present_informal_low, u'지다', u'져'
    yield check, declarative_past_informal_low, u'지다', u'졌어'
    yield check, declarative_future_informal_low, u'지다', u'질거야'
    yield check, inquisitive_present_informal_low, u'지다', u'져'
    yield check, inquisitive_past_informal_low, u'지다', u'졌어'
    yield check, propositive_present_informal_low, u'지다', u'져'
    yield check, declarative_present_informal_high, u'지다', u'져요'
    yield check, declarative_past_informal_high, u'지다', u'졌어요'
    yield check, declarative_present_informal_low, u'지다', u'져'
    yield check, declarative_past_informal_low, u'지다', u'졌어'
    yield check, declarative_future_informal_low, u'지다', u'질거야'
    yield check, inquisitive_present_informal_low, u'지다', u'져'
    yield check, inquisitive_past_informal_low, u'지다', u'졌어'
    yield check, propositive_present_informal_low, u'지다', u'져'
    yield check, declarative_present_informal_high, u'지다', u'져요'
    yield check, declarative_past_informal_high, u'지다', u'졌어요'
    yield check, declarative_present_informal_low, u'지다', u'져'
    yield check, declarative_past_informal_low, u'지다', u'졌어'
    yield check, declarative_future_informal_low, u'지다', u'질거야'
    yield check, inquisitive_present_informal_low, u'지다', u'져'
    yield check, inquisitive_past_informal_low, u'지다', u'졌어'
    yield check, propositive_present_informal_low, u'지다', u'져'
    yield check, declarative_present_informal_high, u'지다', u'져요'
    yield check, declarative_past_informal_high, u'지다', u'졌어요'
    yield check, declarative_present_informal_low, u'지다', u'져'
    yield check, declarative_past_informal_low, u'지다', u'졌어'
    yield check, declarative_future_informal_low, u'지다', u'질거야'
    yield check, inquisitive_present_informal_low, u'지다', u'져'
    yield check, inquisitive_past_informal_low, u'지다', u'졌어'
    yield check, propositive_present_informal_low, u'지다', u'져'
    yield check, declarative_present_informal_high, u'지다', u'져요'
    yield check, declarative_past_informal_high, u'지다', u'졌어요'
    yield check, declarative_present_informal_low, u'가깝다', u'가까워'
    yield check, declarative_past_informal_low, u'가깝다', u'가까웠어'
    yield check, declarative_future_informal_low, u'가깝다', u'가까울거야'
    yield check, inquisitive_present_informal_low, u'가깝다', u'가까워'
    yield check, inquisitive_past_informal_low, u'가깝다', u'가까웠어'
    yield check, declarative_present_informal_high, u'가깝다', u'가까워요'
    yield check, declarative_past_informal_high, u'가깝다', u'가까웠어요'
    yield check, declarative_present_informal_low, u'적다', u'적어'
    yield check, declarative_past_informal_low, u'적다', u'적었어'
    yield check, declarative_future_informal_low, u'적다', u'적을거야'
    yield check, inquisitive_present_informal_low, u'적다', u'적어'
    yield check, inquisitive_past_informal_low, u'적다', u'적었어'
    yield check, propositive_present_informal_low, u'적다', u'적어'
    yield check, declarative_present_informal_high, u'적다', u'적어요'
    yield check, declarative_past_informal_high, u'적다', u'적었어요'
    yield check, declarative_present_informal_low, u'적다', u'적어'
    yield check, declarative_past_informal_low, u'적다', u'적었어'
    yield check, declarative_future_informal_low, u'적다', u'적을거야'
    yield check, inquisitive_present_informal_low, u'적다', u'적어'
    yield check, inquisitive_past_informal_low, u'적다', u'적었어'
    yield check, declarative_present_informal_high, u'적다', u'적어요'
    yield check, declarative_past_informal_high, u'적다', u'적었어요'
    yield check, declarative_present_informal_low, u'남다', u'남아'
    yield check, declarative_past_informal_low, u'남다', u'남았어'
    yield check, declarative_future_informal_low, u'남다', u'남을거야'
    yield check, inquisitive_present_informal_low, u'남다', u'남아'
    yield check, inquisitive_past_informal_low, u'남다', u'남았어'
    yield check, propositive_present_informal_low, u'남다', u'남아'
    yield check, declarative_present_informal_high, u'남다', u'남아요'
    yield check, declarative_past_informal_high, u'남다', u'남았어요'
    yield check, declarative_present_informal_low, u'가다', u'가'
    yield check, declarative_past_informal_low, u'가다', u'갔어'
    yield check, declarative_future_informal_low, u'가다', u'갈거야'
    yield check, inquisitive_present_informal_low, u'가다', u'가'
    yield check, inquisitive_past_informal_low, u'가다', u'갔어'
    yield check, propositive_present_informal_low, u'가다', u'가'
    yield check, declarative_present_informal_high, u'가다', u'가요'
    yield check, declarative_past_informal_high, u'가다', u'갔어요'
    yield check, declarative_present_informal_low, u'내다', u'내'
    yield check, declarative_past_informal_low, u'내다', u'냈어'
    yield check, declarative_future_informal_low, u'내다', u'낼거야'
    yield check, inquisitive_present_informal_low, u'내다', u'내'
    yield check, inquisitive_past_informal_low, u'내다', u'냈어'
    yield check, propositive_present_informal_low, u'내다', u'내'
    yield check, declarative_present_informal_high, u'내다', u'내요'
    yield check, declarative_past_informal_high, u'내다', u'냈어요'
    yield check, declarative_present_informal_low, u'내다', u'내'
    yield check, declarative_past_informal_low, u'내다', u'냈어'
    yield check, declarative_future_informal_low, u'내다', u'낼거야'
    yield check, inquisitive_present_informal_low, u'내다', u'내'
    yield check, inquisitive_past_informal_low, u'내다', u'냈어'
    yield check, propositive_present_informal_low, u'내다', u'내'
    yield check, declarative_present_informal_high, u'내다', u'내요'
    yield check, declarative_past_informal_high, u'내다', u'냈어요'
    yield check, declarative_present_informal_low, u'만들다', u'만들어'
    yield check, declarative_past_informal_low, u'만들다', u'만들었어'
    yield check, declarative_future_informal_low, u'만들다', u'만들거야'
    yield check, inquisitive_present_informal_low, u'만들다', u'만들어'
    yield check, inquisitive_past_informal_low, u'만들다', u'만들었어'
    yield check, propositive_present_informal_low, u'만들다', u'만들어'
    yield check, declarative_present_informal_high, u'만들다', u'만들어요'
    yield check, declarative_past_informal_high, u'만들다', u'만들었어요'
    yield check, declarative_present_informal_low, u'부르다', u'불러'
    yield check, declarative_past_informal_low, u'부르다', u'불렀어'
    yield check, declarative_future_informal_low, u'부르다', u'부를거야'
    yield check, inquisitive_present_informal_low, u'부르다', u'불러'
    yield check, inquisitive_past_informal_low, u'부르다', u'불렀어'
    yield check, propositive_present_informal_low, u'부르다', u'불러'
    yield check, declarative_present_informal_high, u'부르다', u'불러요'
    yield check, declarative_past_informal_high, u'부르다', u'불렀어요'
    yield check, declarative_present_informal_low, u'부르다', u'불러'
    yield check, declarative_past_informal_low, u'부르다', u'불렀어'
    yield check, declarative_future_informal_low, u'부르다', u'부를거야'
    yield check, inquisitive_present_informal_low, u'부르다', u'불러'
    yield check, inquisitive_past_informal_low, u'부르다', u'불렀어'
    yield check, declarative_present_informal_high, u'부르다', u'불러요'
    yield check, declarative_past_informal_high, u'부르다', u'불렀어요'
    yield check, declarative_present_informal_low, u'살다', u'살아'
    yield check, declarative_past_informal_low, u'살다', u'살았어'
    yield check, declarative_future_informal_low, u'살다', u'살거야'
    yield check, inquisitive_present_informal_low, u'살다', u'살아'
    yield check, inquisitive_past_informal_low, u'살다', u'살았어'
    yield check, propositive_present_informal_low, u'살다', u'살아'
    yield check, declarative_present_informal_high, u'살다', u'살아요'
    yield check, declarative_past_informal_high, u'살다', u'살았어요'
    yield check, declarative_present_informal_low, u'살다', u'살아'
    yield check, declarative_past_informal_low, u'살다', u'살았어'
    yield check, declarative_future_informal_low, u'살다', u'살거야'
    yield check, inquisitive_present_informal_low, u'살다', u'살아'
    yield check, inquisitive_past_informal_low, u'살다', u'살았어'
    yield check, declarative_present_informal_high, u'살다', u'살아요'
    yield check, declarative_past_informal_high, u'살다', u'살았어요'
    yield check, declarative_present_informal_low, u'주다', u'줘'
    yield check, declarative_past_informal_low, u'주다', u'줬어'
    yield check, declarative_future_informal_low, u'주다', u'줄거야'
    yield check, inquisitive_present_informal_low, u'주다', u'줘'
    yield check, inquisitive_past_informal_low, u'주다', u'줬어'
    yield check, propositive_present_informal_low, u'주다', u'줘'
    yield check, declarative_present_informal_high, u'주다', u'줘요'
    yield check, declarative_past_informal_high, u'주다', u'줬어요'
    yield check, declarative_present_informal_low, u'외우다', u'외워'
    yield check, declarative_past_informal_low, u'외우다', u'외웠어'
    yield check, declarative_future_informal_low, u'외우다', u'외울거야'
    yield check, inquisitive_present_informal_low, u'외우다', u'외워'
    yield check, inquisitive_past_informal_low, u'외우다', u'외웠어'
    yield check, propositive_present_informal_low, u'외우다', u'외워'
    yield check, declarative_present_informal_high, u'외우다', u'외워요'
    yield check, declarative_past_informal_high, u'외우다', u'외웠어요'
    yield check, declarative_present_informal_low, u'보다', u'봐'
    yield check, declarative_past_informal_low, u'보다', u'봤어'
    yield check, declarative_future_informal_low, u'보다', u'볼거야'
    yield check, inquisitive_present_informal_low, u'보다', u'봐'
    yield check, inquisitive_past_informal_low, u'보다', u'봤어'
    yield check, propositive_present_informal_low, u'보다', u'봐'
    yield check, declarative_present_informal_high, u'보다', u'봐요'
    yield check, declarative_past_informal_high, u'보다', u'봤어요'
    yield check, declarative_present_informal_low, u'까맣다', u'까매'
    yield check, declarative_past_informal_low, u'까맣다', u'까맸어'
    yield check, declarative_future_informal_low, u'까맣다', u'까말거야'
    yield check, inquisitive_present_informal_low, u'까맣다', u'까매'
    yield check, inquisitive_past_informal_low, u'까맣다', u'까맸어'
    yield check, declarative_present_informal_high, u'까맣다', u'까매요'
    yield check, declarative_past_informal_high, u'까맣다', u'까맸어요'
    yield check, declarative_present_informal_low, u'애쓰다', u'애써'
    yield check, declarative_past_informal_low, u'애쓰다', u'애썼어'
    yield check, declarative_future_informal_low, u'애쓰다', u'애쓸거야'
    yield check, inquisitive_present_informal_low, u'애쓰다', u'애써'
    yield check, inquisitive_past_informal_low, u'애쓰다', u'애썼어'
    yield check, propositive_present_informal_low, u'애쓰다', u'애써'
    yield check, declarative_present_informal_high, u'애쓰다', u'애써요'
    yield check, declarative_past_informal_high, u'애쓰다', u'애썼어요'
    yield check, declarative_present_informal_low, u'바르다', u'발라'
    yield check, declarative_past_informal_low, u'바르다', u'발랐어'
    yield check, declarative_future_informal_low, u'바르다', u'바를거야'
    yield check, inquisitive_present_informal_low, u'바르다', u'발라'
    yield check, inquisitive_past_informal_low, u'바르다', u'발랐어'
    yield check, propositive_present_informal_low, u'바르다', u'발라'
    yield check, declarative_present_informal_high, u'바르다', u'발라요'
    yield check, declarative_past_informal_high, u'바르다', u'발랐어요'
    yield check, declarative_present_informal_low, u'바르다', u'발라'
    yield check, declarative_past_informal_low, u'바르다', u'발랐어'
    yield check, declarative_future_informal_low, u'바르다', u'바를거야'
    yield check, inquisitive_present_informal_low, u'바르다', u'발라'
    yield check, inquisitive_past_informal_low, u'바르다', u'발랐어'
    yield check, propositive_present_informal_low, u'바르다', u'발라'
    yield check, declarative_present_informal_high, u'바르다', u'발라요'
    yield check, declarative_past_informal_high, u'바르다', u'발랐어요'
    yield check, declarative_present_informal_low, u'바르다', u'발라'
    yield check, declarative_past_informal_low, u'바르다', u'발랐어'
    yield check, declarative_future_informal_low, u'바르다', u'바를거야'
    yield check, inquisitive_present_informal_low, u'바르다', u'발라'
    yield check, inquisitive_past_informal_low, u'바르다', u'발랐어'
    yield check, declarative_present_informal_high, u'바르다', u'발라요'
    yield check, declarative_past_informal_high, u'바르다', u'발랐어요'
    yield check, declarative_present_informal_low, u'뛰다', u'뛰어'
    yield check, declarative_past_informal_low, u'뛰다', u'뛰었어'
    yield check, declarative_future_informal_low, u'뛰다', u'뛸거야'
    yield check, inquisitive_present_informal_low, u'뛰다', u'뛰어'
    yield check, inquisitive_past_informal_low, u'뛰다', u'뛰었어'
    yield check, propositive_present_informal_low, u'뛰다', u'뛰어'
    yield check, declarative_present_informal_high, u'뛰다', u'뛰어요'
    yield check, declarative_past_informal_high, u'뛰다', u'뛰었어요'
    yield check, declarative_present_informal_low, u'뛰다', u'뛰어'
    yield check, declarative_past_informal_low, u'뛰다', u'뛰었어'
    yield check, declarative_future_informal_low, u'뛰다', u'뛸거야'
    yield check, inquisitive_present_informal_low, u'뛰다', u'뛰어'
    yield check, inquisitive_past_informal_low, u'뛰다', u'뛰었어'
    yield check, propositive_present_informal_low, u'뛰다', u'뛰어'
    yield check, declarative_present_informal_high, u'뛰다', u'뛰어요'
    yield check, declarative_past_informal_high, u'뛰다', u'뛰었어요'
    yield check, declarative_present_informal_low, u'뛰다', u'뛰어'
    yield check, declarative_past_informal_low, u'뛰다', u'뛰었어'
    yield check, declarative_future_informal_low, u'뛰다', u'뛸거야'
    yield check, inquisitive_present_informal_low, u'뛰다', u'뛰어'
    yield check, inquisitive_past_informal_low, u'뛰다', u'뛰었어'
    yield check, propositive_present_informal_low, u'뛰다', u'뛰어'
    yield check, declarative_present_informal_high, u'뛰다', u'뛰어요'
    yield check, declarative_past_informal_high, u'뛰다', u'뛰었어요'
    yield check, declarative_present_informal_low, u'되다', u'돼'
    yield check, declarative_past_informal_low, u'되다', u'됐어'
    yield check, declarative_future_informal_low, u'되다', u'될거야'
    yield check, inquisitive_present_informal_low, u'되다', u'돼'
    yield check, inquisitive_past_informal_low, u'되다', u'됐어'
    yield check, propositive_present_informal_low, u'되다', u'돼'
    yield check, declarative_present_informal_high, u'되다', u'돼요'
    yield check, declarative_past_informal_high, u'되다', u'됐어요'
    yield check, declarative_present_informal_low, u'되다', u'돼'
    yield check, declarative_past_informal_low, u'되다', u'됐어'
    yield check, declarative_future_informal_low, u'되다', u'될거야'
    yield check, inquisitive_present_informal_low, u'되다', u'돼'
    yield check, inquisitive_past_informal_low, u'되다', u'됐어'
    yield check, propositive_present_informal_low, u'되다', u'돼'
    yield check, declarative_present_informal_high, u'되다', u'돼요'
    yield check, declarative_past_informal_high, u'되다', u'됐어요'
    yield check, declarative_present_informal_low, u'되다', u'돼'
    yield check, declarative_past_informal_low, u'되다', u'됐어'
    yield check, declarative_future_informal_low, u'되다', u'될거야'
    yield check, inquisitive_present_informal_low, u'되다', u'돼'
    yield check, inquisitive_past_informal_low, u'되다', u'됐어'
    yield check, propositive_present_informal_low, u'되다', u'돼'
    yield check, declarative_present_informal_high, u'되다', u'돼요'
    yield check, declarative_past_informal_high, u'되다', u'됐어요'
    yield check, declarative_present_informal_low, u'되다', u'돼'
    yield check, declarative_past_informal_low, u'되다', u'됐어'
    yield check, declarative_future_informal_low, u'되다', u'될거야'
    yield check, inquisitive_present_informal_low, u'되다', u'돼'
    yield check, inquisitive_past_informal_low, u'되다', u'됐어'
    yield check, declarative_present_informal_high, u'되다', u'돼요'
    yield check, declarative_past_informal_high, u'되다', u'됐어요'
    yield check, declarative_present_informal_low, u'오다', u'와'
    yield check, declarative_past_informal_low, u'오다', u'왔어'
    yield check, declarative_future_informal_low, u'오다', u'올거야'
    yield check, inquisitive_present_informal_low, u'오다', u'와'
    yield check, inquisitive_past_informal_low, u'오다', u'왔어'
    yield check, propositive_present_informal_low, u'오다', u'와'
    yield check, declarative_present_informal_high, u'오다', u'와요'
    yield check, declarative_past_informal_high, u'오다', u'왔어요'
    yield check, declarative_present_informal_low, u'잇다', u'이어'
    yield check, declarative_past_informal_low, u'잇다', u'이었어'
    yield check, declarative_future_informal_low, u'잇다', u'이을거야'
    yield check, inquisitive_present_informal_low, u'잇다', u'이어'
    yield check, inquisitive_past_informal_low, u'잇다', u'이었어'
    yield check, propositive_present_informal_low, u'잇다', u'이어'
    yield check, declarative_present_informal_high, u'잇다', u'이어요'
    yield check, declarative_past_informal_high, u'잇다', u'이었어요'
    yield check, declarative_present_informal_low, u'잇다', u'이어'
    yield check, declarative_past_informal_low, u'잇다', u'이었어'
    yield check, declarative_future_informal_low, u'잇다', u'이을거야'
    yield check, inquisitive_present_informal_low, u'잇다', u'이어'
    yield check, inquisitive_past_informal_low, u'잇다', u'이었어'
    yield check, propositive_present_informal_low, u'잇다', u'이어'
    yield check, declarative_present_informal_high, u'잇다', u'이어요'
    yield check, declarative_past_informal_high, u'잇다', u'이었어요'
    yield check, declarative_present_informal_low, u'서다', u'서'
    yield check, declarative_past_informal_low, u'서다', u'섰어'
    yield check, declarative_future_informal_low, u'서다', u'설거야'
    yield check, inquisitive_present_informal_low, u'서다', u'서'
    yield check, inquisitive_past_informal_low, u'서다', u'섰어'
    yield check, propositive_present_informal_low, u'서다', u'서'
    yield check, declarative_present_informal_high, u'서다', u'서요'
    yield check, declarative_past_informal_high, u'서다', u'섰어요'
    yield check, declarative_present_informal_low, u'담그다', u'담가'
    yield check, declarative_past_informal_low, u'담그다', u'담갔어'
    yield check, declarative_future_informal_low, u'담그다', u'담글거야'
    yield check, inquisitive_present_informal_low, u'담그다', u'담가'
    yield check, inquisitive_past_informal_low, u'담그다', u'담갔어'
    yield check, propositive_present_informal_low, u'담그다', u'담가'
    yield check, declarative_present_informal_high, u'담그다', u'담가요'
    yield check, declarative_past_informal_high, u'담그다', u'담갔어요'
    yield check, declarative_present_informal_low, u'쓰다', u'써'
    yield check, declarative_past_informal_low, u'쓰다', u'썼어'
    yield check, declarative_future_informal_low, u'쓰다', u'쓸거야'
    yield check, inquisitive_present_informal_low, u'쓰다', u'써'
    yield check, inquisitive_past_informal_low, u'쓰다', u'썼어'
    yield check, propositive_present_informal_low, u'쓰다', u'써'
    yield check, declarative_present_informal_high, u'쓰다', u'써요'
    yield check, declarative_past_informal_high, u'쓰다', u'썼어요'
    yield check, declarative_present_informal_low, u'쓰다', u'써'
    yield check, declarative_past_informal_low, u'쓰다', u'썼어'
    yield check, declarative_future_informal_low, u'쓰다', u'쓸거야'
    yield check, inquisitive_present_informal_low, u'쓰다', u'써'
    yield check, inquisitive_past_informal_low, u'쓰다', u'썼어'
    yield check, propositive_present_informal_low, u'쓰다', u'써'
    yield check, declarative_present_informal_high, u'쓰다', u'써요'
    yield check, declarative_past_informal_high, u'쓰다', u'썼어요'
    yield check, declarative_present_informal_low, u'쓰다', u'써'
    yield check, declarative_past_informal_low, u'쓰다', u'썼어'
    yield check, declarative_future_informal_low, u'쓰다', u'쓸거야'
    yield check, inquisitive_present_informal_low, u'쓰다', u'써'
    yield check, inquisitive_past_informal_low, u'쓰다', u'썼어'
    yield check, propositive_present_informal_low, u'쓰다', u'써'
    yield check, declarative_present_informal_high, u'쓰다', u'써요'
    yield check, declarative_past_informal_high, u'쓰다', u'썼어요'
    yield check, declarative_present_informal_low, u'쓰다', u'써'
    yield check, declarative_past_informal_low, u'쓰다', u'썼어'
    yield check, declarative_future_informal_low, u'쓰다', u'쓸거야'
    yield check, inquisitive_present_informal_low, u'쓰다', u'써'
    yield check, inquisitive_past_informal_low, u'쓰다', u'썼어'
    yield check, propositive_present_informal_low, u'쓰다', u'써'
    yield check, declarative_present_informal_high, u'쓰다', u'써요'
    yield check, declarative_past_informal_high, u'쓰다', u'썼어요'
    yield check, declarative_present_informal_low, u'쓰다', u'써'
    yield check, declarative_past_informal_low, u'쓰다', u'썼어'
    yield check, declarative_future_informal_low, u'쓰다', u'쓸거야'
    yield check, inquisitive_present_informal_low, u'쓰다', u'써'
    yield check, inquisitive_past_informal_low, u'쓰다', u'썼어'
    yield check, propositive_present_informal_low, u'쓰다', u'써'
    yield check, declarative_present_informal_high, u'쓰다', u'써요'
    yield check, declarative_past_informal_high, u'쓰다', u'썼어요'
    yield check, declarative_present_informal_low, u'쓰다', u'써'
    yield check, declarative_past_informal_low, u'쓰다', u'썼어'
    yield check, declarative_future_informal_low, u'쓰다', u'쓸거야'
    yield check, inquisitive_present_informal_low, u'쓰다', u'써'
    yield check, inquisitive_past_informal_low, u'쓰다', u'썼어'
    yield check, declarative_present_informal_high, u'쓰다', u'써요'
    yield check, declarative_past_informal_high, u'쓰다', u'썼어요'
    yield check, declarative_present_informal_low, u'눕다', u'누워'
    yield check, declarative_past_informal_low, u'눕다', u'누웠어'
    yield check, declarative_future_informal_low, u'눕다', u'누울거야'
    yield check, inquisitive_present_informal_low, u'눕다', u'누워'
    yield check, inquisitive_past_informal_low, u'눕다', u'누웠어'
    yield check, propositive_present_informal_low, u'눕다', u'누워'
    yield check, declarative_present_informal_high, u'눕다', u'누워요'
    yield check, declarative_past_informal_high, u'눕다', u'누웠어요'
    yield check, declarative_present_informal_low, u'눕다', u'누워'
    yield check, declarative_past_informal_low, u'눕다', u'누웠어'
    yield check, declarative_future_informal_low, u'눕다', u'누울거야'
    yield check, inquisitive_present_informal_low, u'눕다', u'누워'
    yield check, inquisitive_past_informal_low, u'눕다', u'누웠어'
    yield check, propositive_present_informal_low, u'눕다', u'누워'
    yield check, declarative_present_informal_high, u'눕다', u'누워요'
    yield check, declarative_past_informal_high, u'눕다', u'누웠어요'
    yield check, declarative_present_informal_low, u'눕다', u'누워'
    yield check, declarative_past_informal_low, u'눕다', u'누웠어'
    yield check, declarative_future_informal_low, u'눕다', u'누울거야'
    yield check, inquisitive_present_informal_low, u'눕다', u'누워'
    yield check, inquisitive_past_informal_low, u'눕다', u'누웠어'
    yield check, propositive_present_informal_low, u'눕다', u'누워'
    yield check, declarative_present_informal_high, u'눕다', u'누워요'
    yield check, declarative_past_informal_high, u'눕다', u'누웠어요'
    yield check, declarative_present_informal_low, u'그러다', u'그래'
    yield check, declarative_past_informal_low, u'그러다', u'그랬어'
    yield check, declarative_future_informal_low, u'그러다', u'그럴거야'
    yield check, inquisitive_present_informal_low, u'그러다', u'그래'
    yield check, inquisitive_past_informal_low, u'그러다', u'그랬어'
    yield check, propositive_present_informal_low, u'그러다', u'그래'
    yield check, declarative_present_informal_high, u'그러다', u'그래요'
    yield check, declarative_past_informal_high, u'그러다', u'그랬어요'
    yield check, declarative_present_informal_low, u'푸르다', u'푸르러'
    yield check, declarative_past_informal_low, u'푸르다', u'푸르렀어'
    yield check, declarative_future_informal_low, u'푸르다', u'푸를거야'
    yield check, inquisitive_present_informal_low, u'푸르다', u'푸르러'
    yield check, inquisitive_past_informal_low, u'푸르다', u'푸르렀어'
    yield check, declarative_present_informal_high, u'푸르다', u'푸르러요'
    yield check, declarative_past_informal_high, u'푸르다', u'푸르렀어요'
    yield check, declarative_present_informal_low, u'낫다', u'나아'
    yield check, declarative_past_informal_low, u'낫다', u'나았어'
    yield check, declarative_future_informal_low, u'낫다', u'나을거야'
    yield check, inquisitive_present_informal_low, u'낫다', u'나아'
    yield check, inquisitive_past_informal_low, u'낫다', u'나았어'
    yield check, propositive_present_informal_low, u'낫다', u'나아'
    yield check, declarative_present_informal_high, u'낫다', u'나아요'
    yield check, declarative_past_informal_high, u'낫다', u'나았어요'
    yield check, declarative_present_informal_low, u'낫다', u'나아'
    yield check, declarative_past_informal_low, u'낫다', u'나았어'
    yield check, declarative_future_informal_low, u'낫다', u'나을거야'
    yield check, inquisitive_present_informal_low, u'낫다', u'나아'
    yield check, inquisitive_past_informal_low, u'낫다', u'나았어'
    yield check, declarative_present_informal_high, u'낫다', u'나아요'
    yield check, declarative_past_informal_high, u'낫다', u'나았어요'
    yield check, declarative_present_informal_low, u'누르다', u'눌러'
    yield check, declarative_past_informal_low, u'누르다', u'눌렀어'
    yield check, declarative_future_informal_low, u'누르다', u'누를거야'
    yield check, inquisitive_present_informal_low, u'누르다', u'눌러'
    yield check, inquisitive_past_informal_low, u'누르다', u'눌렀어'
    yield check, propositive_present_informal_low, u'누르다', u'눌러'
    yield check, declarative_present_informal_high, u'누르다', u'눌러요'
    yield check, declarative_past_informal_high, u'누르다', u'눌렀어요'
    yield check, declarative_present_informal_low, u'깨닫다', u'깨달아'
    yield check, declarative_past_informal_low, u'깨닫다', u'깨달았어'
    yield check, declarative_future_informal_low, u'깨닫다', u'깨달을거야'
    yield check, inquisitive_present_informal_low, u'깨닫다', u'깨달아'
    yield check, inquisitive_past_informal_low, u'깨닫다', u'깨달았어'
    yield check, propositive_present_informal_low, u'깨닫다', u'깨달아'
    yield check, declarative_present_informal_high, u'깨닫다', u'깨달아요'
    yield check, declarative_past_informal_high, u'깨닫다', u'깨달았어요'
    yield check, declarative_present_informal_low, u'돕다', u'도와'
    yield check, declarative_past_informal_low, u'돕다', u'도왔어'
    yield check, declarative_future_informal_low, u'돕다', u'도울거야'
    yield check, inquisitive_present_informal_low, u'돕다', u'도와'
    yield check, inquisitive_past_informal_low, u'돕다', u'도왔어'
    yield check, propositive_present_informal_low, u'돕다', u'도와'
    yield check, declarative_present_informal_high, u'돕다', u'도와요'
    yield check, declarative_past_informal_high, u'돕다', u'도왔어요'
    yield check, declarative_present_informal_low, u'아니다', u'아니야'
    yield check, declarative_past_informal_low, u'아니다', u'아니었어'
    yield check, declarative_future_informal_low, u'아니다', u'아닐거야'
    yield check, inquisitive_present_informal_low, u'아니다', u'아니야'
    yield check, inquisitive_past_informal_low, u'아니다', u'아니었어'
    yield check, declarative_present_informal_high, u'아니다', u'아니에요'
    yield check, declarative_past_informal_high, u'아니다', u'아니었어요'
    yield check, declarative_past_informal_low, u'이다', u'였어'
    yield check, declarative_future_informal_low, u'이다', u'일거야'
    yield check, inquisitive_past_informal_low, u'이다', u'였어'
    yield check, declarative_past_informal_high, u'이다', u'였어요'
    yield check, declarative_future_informal_low, u'이다', u'일거야'
    yield check, declarative_present_informal_high, u'이다', u'이에요'
    yield check, declarative_present_informal_low, u'푸다', u'퍼'
    yield check, declarative_past_informal_low, u'푸다', u'펐어'
    yield check, declarative_future_informal_low, u'푸다', u'풀거야'
    yield check, inquisitive_present_informal_low, u'푸다', u'퍼'
    yield check, inquisitive_past_informal_low, u'푸다', u'펐어'
    yield check, propositive_present_informal_low, u'푸다', u'퍼'
    yield check, declarative_present_informal_high, u'푸다', u'퍼요'
    yield check, declarative_past_informal_high, u'푸다', u'펐어요'
