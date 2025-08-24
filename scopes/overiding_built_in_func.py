import builtins

# # Сохраняем оригинальную функцию open
# original = builtins.open
#
#
# def makeopen(id):
#     # Определяем новую версию функции open
#     def custom(*pargs, **kargs):
#         # Логируем вызов новой версии open
#         print('Custom open call %r:' % id, pargs, kargs)
#
#         # Возвращаем результат оригинального вызова open
#         return original(*pargs, **kargs)
#
#     # Перезаписываем глобальную функцию open на нашу кастомную версию
#     builtins.open = custom
#
# #
# # makeopen('hello')
# # open('ex1.py')  # Custom open call 'hello': ('ex1.py',) {}
# #
# # # теперь каждый раз, когда будем вызывать функцию open,
# # # мы будем обращаться к функции custom и выполнять ее логику
# #
# # # здесь мы переопределили поведение обработчика
# # makeopen('hi')
# # open('ex1.py')  # Custom open call 'hi': ('ex1.py',) {}
#
# # ---------------------------------------------------------------------
# # но если оригинальную функцию поместить в makeopen,
# # то в custom рекурсивно будет возвращаться original
# def makeopen2(id):
#     original2 = builtins.open
#
#     def custom(*pargs, **kargs):
#         print('2 Custom open call %r:' % id, pargs, kargs)
#
#         return original2(*pargs, **kargs)
#
#     builtins.open = custom
#
# makeopen2('hello')
# open('overiding_built_in_func.py')
#
# makeopen2('hi')
# open('overiding_built_in_func.py')
#
# # вывод
# # Custom open call 'hello': ('ex1.py',) {}
# # Custom open call 'hi': ('ex1.py',) {}
# # Custom open call 'hello': ('ex1.py',) {}
#
# # чтобы избежать этого, нужно убрать возврат в custom
# -----------------------------------------
# Эквивалент на основе классов
# class Makeopen:
#
#     def __init__ (self, id):
#         self.id = id
#         self.original = builtins.open
#         builtins.open = self
#
#     def __call__(self, *pargs, **kargs):
#         print('Custom open call %r: ' % self.id, pargs, kargs)
#         return self.original(*pargs, **kargs)
#
#
# a = Makeopen(3)
#
# a('overiding_built_in_func.py')