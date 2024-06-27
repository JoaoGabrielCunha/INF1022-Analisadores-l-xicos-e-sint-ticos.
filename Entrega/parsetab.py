
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMULTIPLYrightNEGCOMMA ELSE ENDIF ENQUANTO EQUALS EVAL EXECUTE FACA FIM ID IF INICIO LPAREN MONITOR MULTIPLY NEG NUMBER PLUS RPAREN TERMINO THEN ZEROprograma : INICIO varlist MONITOR monitor EXECUTE cmds TERMINOmonitor : varlist\n               varlist : ID COMMA varlist\n               | IDcmds : cmd cmds\n            | cmdcmd : ID EQUALS expr\n           | ZERO LPAREN ID RPAREN\n           | ENQUANTO ID FACA cmds FIM\n           | IF expr THEN cmds ELSE cmds ENDIF\n           | IF expr THEN cmds ENDIF\n           | EVAL LPAREN expr COMMA expr COMMA cmds RPAREN\n           | EVAL cmds NUMBER FIMexpr : expr PLUS expr\n            | expr MULTIPLY expr\n            | LPAREN expr RPAREN\n            | NUMBER\n            | ID\n            | NEG expr %prec NEG'
    
_lr_action_items = {'INICIO':([0,],[2,]),'$end':([1,18,],[0,-1,]),'ID':([2,5,6,10,12,15,16,17,20,21,24,25,26,27,28,30,32,33,34,35,37,40,43,44,45,46,47,48,49,50,53,54,56,],[4,4,4,13,13,22,26,13,26,31,26,-17,-18,26,26,-7,13,13,26,26,-19,-8,-14,-15,-16,26,-13,-9,13,-11,13,-10,-12,]),'MONITOR':([3,4,9,],[5,-4,-3,]),'COMMA':([4,25,26,37,38,43,44,45,51,],[6,-17,-18,-19,46,-14,-15,-16,53,]),'EXECUTE':([4,7,8,9,],[-4,-2,10,-3,]),'ZERO':([10,12,17,25,26,30,32,33,37,40,43,44,45,47,48,49,50,53,54,56,],[14,14,14,-17,-18,-7,14,14,-19,-8,-14,-15,-16,-13,-9,14,-11,14,-10,-12,]),'ENQUANTO':([10,12,17,25,26,30,32,33,37,40,43,44,45,47,48,49,50,53,54,56,],[15,15,15,-17,-18,-7,15,15,-19,-8,-14,-15,-16,-13,-9,15,-11,15,-10,-12,]),'IF':([10,12,17,25,26,30,32,33,37,40,43,44,45,47,48,49,50,53,54,56,],[16,16,16,-17,-18,-7,16,16,-19,-8,-14,-15,-16,-13,-9,16,-11,16,-10,-12,]),'EVAL':([10,12,17,25,26,30,32,33,37,40,43,44,45,47,48,49,50,53,54,56,],[17,17,17,-17,-18,-7,17,17,-19,-8,-14,-15,-16,-13,-9,17,-11,17,-10,-12,]),'TERMINO':([11,12,19,25,26,30,37,40,43,44,45,47,48,50,54,56,],[18,-6,-5,-17,-18,-7,-19,-8,-14,-15,-16,-13,-9,-11,-10,-12,]),'NUMBER':([12,16,19,20,24,25,26,27,28,29,30,34,35,37,40,43,44,45,46,47,48,50,54,56,],[-6,25,-5,25,25,-17,-18,25,25,39,-7,25,25,-19,-8,-14,-15,-16,25,-13,-9,-11,-10,-12,]),'FIM':([12,19,25,26,30,37,39,40,41,43,44,45,47,48,50,54,56,],[-6,-5,-17,-18,-7,-19,47,-8,48,-14,-15,-16,-13,-9,-11,-10,-12,]),'ELSE':([12,19,25,26,30,37,40,42,43,44,45,47,48,50,54,56,],[-6,-5,-17,-18,-7,-19,-8,49,-14,-15,-16,-13,-9,-11,-10,-12,]),'ENDIF':([12,19,25,26,30,37,40,42,43,44,45,47,48,50,52,54,56,],[-6,-5,-17,-18,-7,-19,-8,50,-14,-15,-16,-13,-9,-11,54,-10,-12,]),'RPAREN':([12,19,25,26,30,31,36,37,40,43,44,45,47,48,50,54,55,56,],[-6,-5,-17,-18,-7,40,45,-19,-8,-14,-15,-16,-13,-9,-11,-10,56,-12,]),'EQUALS':([13,],[20,]),'LPAREN':([14,16,17,20,24,27,28,34,35,46,],[21,24,28,24,24,24,24,24,24,24,]),'NEG':([16,20,24,27,28,34,35,46,],[27,27,27,27,27,27,27,27,]),'FACA':([22,],[32,]),'THEN':([23,25,26,37,43,44,45,],[33,-17,-18,-19,-14,-15,-16,]),'PLUS':([23,25,26,30,36,37,38,43,44,45,51,],[34,-17,-18,34,34,-19,34,-14,-15,-16,34,]),'MULTIPLY':([23,25,26,30,36,37,38,43,44,45,51,],[35,-17,-18,35,35,-19,35,-14,-15,-16,35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'varlist':([2,5,6,],[3,7,9,]),'monitor':([5,],[8,]),'cmds':([10,12,17,32,33,49,53,],[11,19,29,41,42,52,55,]),'cmd':([10,12,17,32,33,49,53,],[12,12,12,12,12,12,12,]),'expr':([16,20,24,27,28,34,35,46,],[23,30,36,37,38,43,44,51,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> INICIO varlist MONITOR monitor EXECUTE cmds TERMINO','programa',7,'p_programa','main.py',74),
  ('monitor -> varlist','monitor',1,'p_monitor','main.py',78),
  ('varlist -> ID COMMA varlist','varlist',3,'p_varlist','main.py',88),
  ('varlist -> ID','varlist',1,'p_varlist','main.py',89),
  ('cmds -> cmd cmds','cmds',2,'p_cmds','main.py',102),
  ('cmds -> cmd','cmds',1,'p_cmds','main.py',103),
  ('cmd -> ID EQUALS expr','cmd',3,'p_cmd','main.py',111),
  ('cmd -> ZERO LPAREN ID RPAREN','cmd',4,'p_cmd','main.py',112),
  ('cmd -> ENQUANTO ID FACA cmds FIM','cmd',5,'p_cmd','main.py',113),
  ('cmd -> IF expr THEN cmds ELSE cmds ENDIF','cmd',7,'p_cmd','main.py',114),
  ('cmd -> IF expr THEN cmds ENDIF','cmd',5,'p_cmd','main.py',115),
  ('cmd -> EVAL LPAREN expr COMMA expr COMMA cmds RPAREN','cmd',8,'p_cmd','main.py',116),
  ('cmd -> EVAL cmds NUMBER FIM','cmd',4,'p_cmd','main.py',117),
  ('expr -> expr PLUS expr','expr',3,'p_expr','main.py',146),
  ('expr -> expr MULTIPLY expr','expr',3,'p_expr','main.py',147),
  ('expr -> LPAREN expr RPAREN','expr',3,'p_expr','main.py',148),
  ('expr -> NUMBER','expr',1,'p_expr','main.py',149),
  ('expr -> ID','expr',1,'p_expr','main.py',150),
  ('expr -> NEG expr','expr',2,'p_expr','main.py',151),
]