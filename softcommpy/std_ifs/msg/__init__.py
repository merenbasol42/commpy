from .simple import MTSimple as __MTSimple

'''one field "data"'''

class Empty(__MTSimple[None]): pass #hiçbir şey göndermeyeceğime namusum ve şerefim üzerine and içerim
class Int(__MTSimple[int]): pass
class Float(__MTSimple[float]): pass
class String(__MTSimple[str]): pass
class Bool(__MTSimple[bool]): pass

class List(__MTSimple[list]): pass
class ListInt(__MTSimple[list[int]]): pass
class ListFloat(__MTSimple[list[float]]): pass
class ListString(__MTSimple[list[str]]): pass
