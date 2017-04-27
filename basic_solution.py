from koneroj import*
basic_solution = writable_concept("Basic Solution")
basic_solution.parts["Definition"].desplay +=r"""
For a system of linear equations with a rank of n defining m veriable where m>n, a basic solution is one of the many solutions to the system, which can be found be setting m-n of the veriables to zero.
\footnote{This is note nessesarly an actually solution to the system if the system has other constraints such as none negativity} """ 
basic_solution.write_module_doc()   
