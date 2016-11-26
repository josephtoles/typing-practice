;; typing practice in lisp

(defparameter characters
  "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()`~-=[]\;',./_+{}|:\"<>? ")

(defun random-characters (n)
  "Returns a string of random characters of length n"
  (if (eql n 0)
      (return-from random-characters ""))
  (if (eql n 1)
      (setf chars-to-test (remove #\  characters))
      (setf chars-to-test characters))
  (concatenate 'string
               (string (char chars-to-test
                             (random (length chars-to-test))))
               (random-characters (decf n))))

; Code to handle Ctrl+C, requires cffi, installed as cl-cffi

;(defmacro set-signal-handler (signo &body body)
;  (let ((handler (gensym "HANDLER")))
;    `(progn
;       (cffi:defcallback ,handler :void ((signo :int))
;         (declare (ignore signo))
;         ,@body)
;       (cffi:foreign-funcall "signal" :int ,signo :pointer (cffi:callback ,handler)))))

;(set-signal-handler 2
;  (format t "Quitting lol!!!11~%")
  ;; fictional function that lets the app know to quit cleanly (don't quit from callback)
;  (signal-app-to-quit))

;; main loop

(add-signal-handler 2 'foo)

(loop (setf text (random-characters 16))
      (format t "~a~%" text)
      (loop (if (equal (read-line *query-io*)
                        text)
                (return))))
  
