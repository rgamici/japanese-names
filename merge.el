(defun merge-dict ()
  (interactive)
  (setq moreLines t)
  (setq filename "merge-result")
  ;; (append-to-file "teststring" nil filename)
  (goto-char 1)
  (re-search-forward "^\\(.*?\\) \\[\\(.*?\\)\\] /(m) \\(.*?\\)/")
  (setq cur-kanj (match-string 1))
  (setq cur-read (match-string 2))
  (setq cur-roma (match-string 3))
  (forward-line 1)
  (while moreLines
    (re-search-forward "^\\(.*?\\) \\[\\(.*?\\)\\] /(m) \\(.*?\\)/" nil t)
    (setq next-kanj (match-string 1))
    (setq next-read (match-string 2))
    (setq next-roma (match-string 3))  
    (if (string= cur-kanj next-kanj)
	(if (not (string-match-p next-read cur-read))
	    ;; same kanji different reading
	    (progn
	      (setq cur-read (concat cur-read " " next-read))
	      (setq cur-roma (concat cur-roma " " next-roma))
	      ))
      ;; diffent kanji
      (append-to-file (concat cur-kanj " [" cur-read "] /(m) " cur-roma "/\n")
		      nil filename)  ;; write to file
      (setq cur-kanj next-kanj)  ;; get new entry to compare 
      (setq cur-read next-read)
      (setq cur-roma next-roma)
      )
    (setq moreLines (= 0 (forward-line 1)))
    )
  (append-to-file (concat cur-kanj " [" cur-read "] /(m) " cur-roma "/\n")
		  nil filename)  ;; write to file
  )

