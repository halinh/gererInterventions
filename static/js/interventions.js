var app = angular.module('interventions', []);

app.controller('interventionsController', function($scope,$http){
    $http.get('/api/interventions/').then(function(response){
        $scope.interventionList=[];
        var today = new Date().toISOString().slice(0,10);
        var todayDate = new Date(today).getTime();

        for (var i=0; i< response.data.length; i++) {
            var intervention ={};
            intervention.id = response.data[i].id
            intervention.libelle = response.data[i].libelle
            intervention.description = response.data[i].description
            intervention.intervenant = response.data[i].nom_intervenant
            intervention.lieu = response.data[i].lieu
            intervention.date = response.data[i].date

            var interventionDate = new Date(intervention.date).getTime();

            if (!(intervention.libelle == "") && !(intervention.description == "") && !(intervention.intervenant == "")
                && !(intervention.lieu == "") && !(intervention.date == "")) {
                     if (interventionDate<=todayDate) {
                        intervention.status="Terminé";
                    } else if (interventionDate>todayDate) {
                        intervention.status="Validé";
                    }

            } else {
                intervention.status="Brouillon";
            }
            intervention.featured = response.data[i].featured
            $scope.interventionList.push(intervention);
        }
    });

    $scope.saveData = function() {
        var data = {
            libelle: $scope.interventionLibelle,
            description: $scope.interventionDesp,
            nom_intervenant: $scope.interventionIntervenant,
            lieu: $scope.interventionLieu,
            date: JSON.stringify($scope.interventionDate).substring(1,11),
            featured:false};
        $http.put('/api/interventions/',data)
    };

    $scope.interventionAdd = function() {
        $scope.interventionList.push({
            libelle: $scope.interventionLibelle,
            description: $scope.interventionDesp,
            intervenant: $scope.interventionIntervenant,
            lieu: $scope.interventionLieu,
            date: JSON.stringify($scope.interventionDate).substring(1,11),
            featured:false});
        $scope.interventionLibelle = '';
        $scope.interventionDescp = '';
        $scope.interventionIntervenant = '';
        $scope.interventionLieu = '';
        $scope.interventionDate = '';
    };

    $scope.interventionRemove = function() {
        var oldList = $scope.interventionList;
        $scope.interventionList = [];
        angular.forEach(oldList, function(intervention) {
            if (intervention.featured) {
                $http.delete('/api/interventions/'+intervention.id+'/');
            } else {
                $scope.interventionList.push(intervention);
            }
        })
    };

    $scope.modify = function(){
        console.log("hello")
    }

})


