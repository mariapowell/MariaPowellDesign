'use strict';

app.controller('UserController',
    function UserController($scope, getUser) {
        $scope.user = {};

        $scope.test = function() {
            return getUser.test("Does it work?");
        }

    }
);
