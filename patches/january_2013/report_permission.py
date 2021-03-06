import webnotes
def execute():
	webnotes.reload_doc("core", "doctype", "docperm")
	webnotes.conn.sql("""update tabDocPerm set `report`=`read`""")

	# no report for singles
	webnotes.conn.sql("""update tabDocPerm, tabDocType set tabDocPerm.`report`=0
		where tabDocPerm.`parent` = tabDocType.name
		and ifnull(tabDocType.issingle,0) = 1""")

	# no submit for not submittables
	webnotes.conn.sql("""update tabDocPerm, tabDocType set tabDocPerm.`submit`=0
		where tabDocPerm.`parent` = tabDocType.name
		and ifnull(tabDocType.is_submittable,0) = 0""")		