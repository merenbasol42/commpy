from .simple import MTSimple as _MTSimple

'''one field "data"'''

class Empty(_MTSimple[None]): pass #hiçbir şey göndermeyeceğime namusum ve şerefim üzerine and içerim
class Int(_MTSimple[int]): pass
class Float(_MTSimple[float]): pass
class String(_MTSimple[str]): pass
class Bool(_MTSimple[bool]): pass

class List(_MTSimple[list]): pass
class ListInt(_MTSimple[list[int]]): pass
class ListFloat(_MTSimple[list[float]]): pass
class ListString(_MTSimple[list[str]]): pass
