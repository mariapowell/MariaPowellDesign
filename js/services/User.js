app.factory('getUser', function () {
	return {
		test: function (string) {
			var test = string + "  yes it works";
			return test;
		}
	};
});