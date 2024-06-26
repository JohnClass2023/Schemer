import sys
import os

compile_pass = [
"""
""",

# a1
"""
(compiler-passes '(
    verify-scheme
    generate-x86-64
))
""",

# a2
"""
(compiler-passes '(
    verify-scheme
    expose-frame-var
    flatten-program
    generate-x86-64
))
""",

# a3
"""
(compiler-passes '(
    verify-scheme
    finalize-locations
    expose-frame-var
    expose-basic-blocks
    flatten-program
    generate-x86-64
))
""",

# a4
"""
(compiler-passes '(
    verify-scheme
    uncover-register-conflict
    assign-registers
    discard-call-live
    finalize-locations
    expose-frame-var
    expose-basic-blocks
    flatten-program
    generate-x86-64
))
""",

# a5
"""
(compiler-passes '(
  verify-scheme
  uncover-frame-conflict
  introduce-allocation-forms
  (iterate
    select-instructions
    uncover-register-conflict
    assign-registers
    (break when everybody-home?)
    assign-frame
    finalize-frame-locations)
  discard-call-live
  finalize-locations
  expose-frame-var
  expose-basic-blocks
  flatten-program
  generate-x86-64
))
""",

# a6
"""
(compiler-passes '(
  verify-scheme
  remove-complex-opera*
  flatten-set!
  impose-calling-conventions
  uncover-frame-conflict
  introduce-allocation-forms
  (iterate
    select-instructions
    uncover-register-conflict
    assign-registers
    (break when everybody-home?)
    assign-frame
    finalize-frame-locations)
  discard-call-live
  finalize-locations
  expose-frame-var
  expose-basic-blocks
  flatten-program
  generate-x86-64
))
""",

# a7
"""
(compiler-passes '(
  verify-scheme
  remove-complex-opera*
  flatten-set!
  impose-calling-conventions
  uncover-frame-conflict
  pre-assign-frame
  assign-new-frame
  (iterate
    finalize-frame-locations
    select-instructions
    uncover-register-conflict
    assign-registers
    (break when everybody-home?)
    assign-frame)
  discard-call-live
  finalize-locations
  expose-frame-var
  expose-basic-blocks
  flatten-program
  generate-x86-64
))
""",

# a8
"""
(compiler-passes '(
  verify-uil
  remove-complex-opera*
  flatten-set!
  impose-calling-conventions
  expose-allocation-pointer
  uncover-frame-conflict
  pre-assign-frame
  assign-new-frame
  (iterate
    finalize-frame-locations
    select-instructions
    uncover-register-conflict
    assign-registers
    (break when everybody-home?)
    assign-frame)
  discard-call-live
  finalize-locations
  expose-frame-var
  expose-memory-operands
  expose-basic-blocks
  flatten-program
  generate-x86-64
))
""",

# a9
"""
(compiler-passes '(
  verify-scheme
  uncover-locals
  remove-let
  verify-uil
  remove-complex-opera*
  flatten-set!
  impose-calling-conventions
  expose-allocation-pointer
  uncover-frame-conflict
  pre-assign-frame
  assign-new-frame
  (iterate
    finalize-frame-locations
    select-instructions
    uncover-register-conflict
    assign-registers
    (break when everybody-home?)
    assign-frame)
  discard-call-live
  finalize-locations
  expose-frame-var
  expose-memory-operands
  expose-basic-blocks
  flatten-program
  generate-x86-64
))
""",

# a10
"""
(compiler-passes '(
  verify-scheme
  specify-representation
  uncover-locals
  remove-let
  verify-uil
  remove-complex-opera*
  flatten-set!
  impose-calling-conventions
  expose-allocation-pointer
  uncover-frame-conflict
  pre-assign-frame
  assign-new-frame
  (iterate
    finalize-frame-locations
    select-instructions
    uncover-register-conflict
    assign-registers
    (break when everybody-home?)
    assign-frame)
  discard-call-live
  finalize-locations
  expose-frame-var
  expose-memory-operands
  expose-basic-blocks
  flatten-program
  generate-x86-64
))
""",

# a11
"""
(compiler-passes '(
  verify-scheme
  lift-letrec
  normalize-context
  specify-representation
  uncover-locals
  remove-let
  verify-uil
  remove-complex-opera*
  flatten-set!
  impose-calling-conventions
  expose-allocation-pointer
  uncover-frame-conflict
  pre-assign-frame
  assign-new-frame
  (iterate
    finalize-frame-locations
    select-instructions
    uncover-register-conflict
    assign-registers
    (break when everybody-home?)
    assign-frame)
  discard-call-live
  finalize-locations
  expose-frame-var
  expose-memory-operands
  expose-basic-blocks
  optimize-jumps
  flatten-program
  generate-x86-64
))
""",

# a12
"""
(compiler-passes '(
  verify-scheme
  uncover-free
  convert-closures
  introduce-procedure-primitives
  lift-letrec
  normalize-context
  specify-representation
  uncover-locals
  remove-let
  verify-uil
  remove-complex-opera*
  flatten-set!
  impose-calling-conventions
  expose-allocation-pointer
  uncover-frame-conflict
  pre-assign-frame
  assign-new-frame
  (iterate
    finalize-frame-locations
    select-instructions
    uncover-register-conflict
    assign-registers
    (break when everybody-home?)
    assign-frame)
  discard-call-live
  finalize-locations
  expose-frame-var
  expose-memory-operands
  expose-basic-blocks
  optimize-jumps
  flatten-program
  generate-x86-64
))
""",

# a13
"""
(compiler-passes '(
  verify-scheme
  optimize-direct-call
  remove-anonymous-lambda
  sanitize-binding-forms
  uncover-free
  convert-closures
  optimize-known-call
  introduce-procedure-primitives
  lift-letrec
  normalize-context
  specify-representation
  uncover-locals
  remove-let
  verify-uil
  remove-complex-opera*
  flatten-set!
  impose-calling-conventions
  expose-allocation-pointer
  uncover-frame-conflict
  pre-assign-frame
  assign-new-frame
  (iterate
    finalize-frame-locations
    select-instructions
    uncover-register-conflict
    assign-registers
    (break when everybody-home?)
    assign-frame)
  discard-call-live
  finalize-locations
  expose-frame-var
  expose-memory-operands
  expose-basic-blocks
  optimize-jumps
  flatten-program
  generate-x86-64
))
""",

# a14
"""
(compiler-passes '(
  verify-scheme
  convert-complex-datum
  uncover-assigned
  purify-letrec
  convert-assignments
  optimize-direct-call
  remove-anonymous-lambda
  sanitize-binding-forms
  uncover-free
  convert-closures
  optimize-known-call
  introduce-procedure-primitives
  lift-letrec
  normalize-context
  specify-representation
  uncover-locals
  remove-let
  verify-uil
  remove-complex-opera*
  flatten-set!
  impose-calling-conventions
  expose-allocation-pointer
  uncover-frame-conflict
  pre-assign-frame
  assign-new-frame
  (iterate
    finalize-frame-locations
    select-instructions
    uncover-register-conflict
    assign-registers
    (break when everybody-home?)
    assign-frame)
  discard-call-live
  finalize-locations
  expose-frame-var
  expose-memory-operands
  expose-basic-blocks
  optimize-jumps
  flatten-program
  generate-x86-64
))
""",

# a15
"""
(compiler-passes '(
  parse-scheme
  convert-complex-datum
  uncover-assigned
  purify-letrec
  convert-assignments
  optimize-direct-call
  remove-anonymous-lambda
  sanitize-binding-forms
  uncover-free
  convert-closures
  optimize-known-call
  introduce-procedure-primitives
  lift-letrec
  normalize-context
  specify-representation
  uncover-locals
  remove-let
  verify-uil
  remove-complex-opera*
  flatten-set!
  impose-calling-conventions
  expose-allocation-pointer
  uncover-frame-conflict
  pre-assign-frame
  assign-new-frame
  (iterate
    finalize-frame-locations
    select-instructions
    uncover-register-conflict
    assign-registers
    (break when everybody-home?)
    assign-frame)
  discard-call-live
  finalize-locations
  expose-frame-var
  expose-memory-operands
  expose-basic-blocks
  optimize-jumps
  flatten-program
  generate-x86-64
))
"""
]

def main():
    arguments = sys.argv[1 : ]
    with open("test.scm", "w") as file:
        task = arguments[0]
        task_id = int(task[task.index("a") + 1 : ])
        compile_passes = compile_pass[task_id]
        file.write(
f"""
(eval-when (compile load eval)
  (optimize-level 2)
  (case-sensitive #t)
)

(load "lib/match.scm")
(load "lib/helpers.scm")
(load "build/fmts.pretty")
(load "build/driver.scm")
(load "build/build.scm")

(load "src/schemer.scm")
(load "{task}/{task}-wrapper.scm")

(define-who everybody-home?
    (define all-home?
        (lambda (body)
            (match body
                [(locals (,local* ...)
                    (ulocals (,ulocals* ...)
                        (spills (,spill* ...)
                            (locate (,home* ...)
                                (frame-conflict, ct ,tail))))) #f]
                [(locate (,home* ...) ,tail) #t]
                [,x (error who "invalid Body ~s" x)])))
    (lambda (x)
        (match x
            [(letrec ([,label* (lambda () ,body*)] ...) ,body)
                (andmap all-home? `(,body ,body* ...))]
            [,x (error who "invalid Program ~s" x)])))

{compile_passes}

(load "{task}/tests{task_id}.scm")
""")
        file.flush()
    return

if __name__ == "__main__":
    main()
