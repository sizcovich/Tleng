
# D:\UBA - DC\Teoria de Lenguajes\Repo\TP2\entregable\src\parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.5'

_lr_method = 'LALR'

_lr_signature = 'A778735C716C761449831BB4ADD0A864'
    
_lr_action_items = {'NOTE':([37,51,54,60,61,],[41,41,41,41,41,]),'TONE':([45,],[49,]),'CONST_ID':([8,19,34,52,],[13,24,24,24,]),'CONST':([5,20,21,25,],[8,-3,8,8,]),'LPAREN':([15,30,40,41,],[19,34,44,45,]),'SEMICOLON':([21,51,60,],[25,54,61,]),'RPAREN':([22,23,24,38,48,59,],[27,-8,-9,43,51,60,]),'BAR':([4,29,31,46,47,53,],[7,33,33,-12,33,-13,]),'TEMPO':([3,],[6,]),'EQUALS':([13,],[18,]),'RBRACE':([29,31,32,35,42,46,47,50,51,53,54,55,57,60,61,62,63,],[-10,-10,36,-11,46,-12,-10,53,-22,-13,-15,-24,-17,-21,-14,-23,-16,]),'REPEAT':([29,31,46,47,53,],[30,30,-12,30,-13,]),'NUM':([6,7,11,17,18,19,34,52,],[10,12,16,20,21,23,23,23,]),'COMMA':([23,24,49,56,],[-8,-9,52,58,]),'FIG':([6,44,58,],[11,48,59,]),'SLASH':([12,],[17,]),'LBRACE':([27,33,43,],[29,37,47,]),'NUMERAL':([0,2,10,11,16,],[3,4,-19,-18,-2,]),'VOICE':([5,9,20,21,25,26,28,36,],[-4,15,-3,-4,-4,-20,-5,15,]),'SILENCE':([37,51,54,60,61,],[40,40,40,40,40,]),'$end':([1,5,9,14,20,21,25,26,28,36,39,],[0,-4,-6,-1,-3,-4,-4,-20,-5,-6,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'song_declaration':([0,],[1,]),'const_dict':([5,21,25,],[9,26,28,]),'voice_list':([9,36,],[14,39,]),'tempo_declaration':([0,],[2,]),'num_or_const_id':([19,34,52,],[22,38,56,]),'bar_or_repeat':([29,31,47,],[31,31,31,]),'voice_content':([29,31,47,],[32,35,50,]),'time_signature_declaration':([2,],[5,]),'bar_content':([37,51,54,60,61,],[42,55,57,62,63,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> song_declaration","S'",1,None,None,None),
  ('song_declaration -> tempo_declaration time_signature_declaration const_dict voice_list','song_declaration',4,'p_song_declaration','parser_rules.py',8),
  ('tempo_declaration -> NUMERAL TEMPO FIG NUM','tempo_declaration',4,'p_tempo','parser_rules.py',12),
  ('time_signature_declaration -> NUMERAL BAR NUM SLASH NUM','time_signature_declaration',5,'p_time_signature','parser_rules.py',16),
  ('const_dict -> <empty>','const_dict',0,'p_const_dict_empty','parser_rules.py',20),
  ('const_dict -> CONST CONST_ID EQUALS NUM SEMICOLON const_dict','const_dict',6,'p_const_dict_append','parser_rules.py',25),
  ('voice_list -> <empty>','voice_list',0,'p_voice_list_empty','parser_rules.py',35),
  ('voice_list -> VOICE LPAREN num_or_const_id RPAREN LBRACE voice_content RBRACE voice_list','voice_list',8,'p_voice_list_append','parser_rules.py',39),
  ('num_or_const_id -> NUM','num_or_const_id',1,'p_num_or_const_id_from_num','parser_rules.py',43),
  ('num_or_const_id -> CONST_ID','num_or_const_id',1,'p_num_or_const_id_from_const_id','parser_rules.py',47),
  ('voice_content -> <empty>','voice_content',0,'p_voice_content_empty','parser_rules.py',56),
  ('voice_content -> bar_or_repeat voice_content','voice_content',2,'p_voice_content_append','parser_rules.py',63),
  ('bar_or_repeat -> BAR LBRACE bar_content RBRACE','bar_or_repeat',4,'p_bar_or_repeat_from_bar','parser_rules.py',67),
  ('bar_or_repeat -> REPEAT LPAREN num_or_const_id RPAREN LBRACE voice_content RBRACE','bar_or_repeat',7,'p_bar_or_repeat_from_repeat','parser_rules.py',71),
  ('bar_content -> NOTE LPAREN TONE COMMA num_or_const_id COMMA FIG RPAREN SEMICOLON','bar_content',9,'p_bar_content_from_note','parser_rules.py',75),
  ('bar_content -> SILENCE LPAREN FIG RPAREN SEMICOLON','bar_content',5,'p_bar_content_from_silence','parser_rules.py',79),
  ('bar_content -> NOTE LPAREN TONE COMMA num_or_const_id COMMA FIG RPAREN SEMICOLON bar_content','bar_content',10,'p_bar_content_append_note','parser_rules.py',83),
  ('bar_content -> SILENCE LPAREN FIG RPAREN SEMICOLON bar_content','bar_content',6,'p_bar_content_append_silence','parser_rules.py',87),
  ('tempo_declaration -> NUMERAL TEMPO FIG','tempo_declaration',3,'p_error_tempo_without_num','parser_rules.py',92),
  ('tempo_declaration -> NUMERAL TEMPO NUM','tempo_declaration',3,'p_error_tempo_without_fig','parser_rules.py',97),
  ('const_dict -> CONST CONST_ID EQUALS NUM const_dict','const_dict',5,'p_error_const_dict_append_without_semicolon','parser_rules.py',102),
  ('bar_content -> NOTE LPAREN TONE COMMA num_or_const_id COMMA FIG RPAREN','bar_content',8,'p_error_bar_content_from_note_without_semicolon','parser_rules.py',107),
  ('bar_content -> SILENCE LPAREN FIG RPAREN','bar_content',4,'p_error_bar_content_from_silence_without_semicolon','parser_rules.py',112),
  ('bar_content -> NOTE LPAREN TONE COMMA num_or_const_id COMMA FIG RPAREN bar_content','bar_content',9,'p_error_bar_content_append_note_without_semicolon','parser_rules.py',117),
  ('bar_content -> SILENCE LPAREN FIG RPAREN bar_content','bar_content',5,'p_error_bar_content_append_silence_without_semicolon','parser_rules.py',122),
]
