

app.controller('menuController', [
	'$scope',
	function($scope){
		$scope.model = { title: "Our Menu"};

		
		$scope.addItem = function(item, price){
			$scope.model.orderedItem = item;
			$scope.model.price = price;
		}
		
	}
	]);

app2.controller('contactControl', [
	'$scope',
	function($scope){
		$scope.model = { title: "Contact"};
		
		$scope.submit = function(model) {
			alert( 'Thank you, we will contact you soon')
			$scope.model = {};
        }

        $scope.reset = function(model) {
            $scope.model = {};

        }
		
		
	}
	]);



