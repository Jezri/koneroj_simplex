from koneroj import *

replace_unbounded_veriable = writable_technique("Replace unbounded veriable")
replace_unbounded_veriable.parts["Procedure"].desplay += r""" If we have a veriable $x$ which is not definitly positive we can replace with two deinifitly positive veriables $$x \prime -x \prime \prime \quad \text{where}\quad x \prime, x \prime \prime \geq 0 $$ """ 
replace_unbounded_veriable.write_module_doc()
