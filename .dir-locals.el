;; Per-directory local variables for GNU Emacs 23 and later.

((nil
  . ((fill-column . 78)
     (tab-width   .  4)
     (ispell-check-comments . exclusive)
     (ispell-local-dictionary . "american")
     (safe-local-variable-values
	  '(sentence-end-double-space . f)
	  (eval add-hook 'prog-mode-hook #'flyspell-prog-mode)
	  (flyspell-issue-message-flag . f) ; avoid messages for every word
)))
 (python-mode
  . ((indent-tabs-mode . nil)))
 (emacs-lisp-mode . ((indent-tabs-mode . nil)))
 (rst-mode
  . ((indent-tabs-mode . nil)
     (fill-column . 78))))
