(*
ofpy
Python script for sending tasks to OmniFocus from Linux
ofpy_hazel.applescript is a part of using Mac OSX as a "client" for the script
Details at http://n8henrie.com/2014/09/ofpy
*)

-- Hazel testing template, originally posted at http://n8henrie.com/2013/02/how-to-test-hazel-applescripts-in-applescript-editor
-- uncomment below for testing Noodlesoft Hazel script in Applescript Editor

-- property theFile : alias "Path:To:ofpy:test_taskfile.txt"
-- hazelProcessFile(theFile)

on hazelProcessFile(theFile)
	
	set ts to do shell script "basename " & quoted form of POSIX path of theFile & " .txt"
	
	set the_task to do shell script "head -n 1 " & quoted form of POSIX path of theFile
	set the_note to do shell script "tail -n +2 " & quoted form of POSIX path of theFile
	
	set the_note_stamped to the_note & return & return & "Created at: " & ts & return & "Imported on " & ((current date) as string)
	
	tell application "OmniFocus"
		tell front document
			
			set new_task to make new inbox task with properties {name:the_task, note:the_note_stamped}
		end tell
	end tell
	
end hazelProcessFile