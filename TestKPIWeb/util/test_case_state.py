from singleton_decorator import singleton


@singleton
class TestCaseState(object):

	def __init__(self, is_set):
		super().__init__()
		self.__is_set = is_set

	def get_is_set(self):
		return self.__is_set

	def set_is_set(self, is_set):
		self.__is_set = is_set
