from koneroj import *
from replace_unbounded_veriable import*
move_solution_to_positive_sector = writable_technique("Move solution to positive sector")
move_solution_to_positive_sector.parts["Procedure"].desplay+=r"""$$"""
move_solution_to_positive_sector.parts["Procedure"].add_technique(replace_unbounded_veriable,r"""\text{ Replace all unbounded or negative veriable with positive ones}""")
move_solution_to_positive_sector.parts["Procedure"].desplay +=r"""$$"""
move_solution_to_positive_sector.write_module_doc()
