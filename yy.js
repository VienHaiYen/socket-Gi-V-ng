var postAPI = "http://ip-api.com/json/?fields=61439"

fetch(postAPI)
	.then(function(response){
		if(response.ok){
            console.log('Successful')
            return response.json();
        }
		else {
            console.log('Failed')}
    })
    .then(function(posts){
	    console.log(posts)
    })
