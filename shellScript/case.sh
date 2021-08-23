fruit="grape"
case $fruit in
	apple)
		echo "これはりんごです."
		;;
	orange)
		echo "これはみかんです."
		;;
	babana|grape)
		echo "これはバナナかぶどうです."
		;;
	*)
		echo "これはりんごでもみかんでもバナナでもぶどうでもありません."
		;;
esac
