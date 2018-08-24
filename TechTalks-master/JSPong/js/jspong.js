window.onload = function(){

    //setting up the canvas and the ctx
    var canvas = document.getElementById("Canvas");
    canvas.width = window.innerWidth * .6;
    canvas.height = window.innerHeight * .6;

    // context to a canvas
    var ctx = canvas.getContext("2d");

    // game objects
    var ball = new Ball(canvas.width/2, canvas.height/2, 5);
    var player = new Player(10, canvas.height/2, 10, 100);
    //var enemy = new Enemy(canvas.width - 20, canvas.height/2, 10, 100, ball);

    // canvas mouse event
    canvas.addEventListener('mousemove', function(evt){
	    var mouseCoords = getMouseCoordinates(evt);
	    player.update(mouseCoords.y);
	});

    // get mouse coordinates
    function getMouseCoordinates(evt){
		var rect = canvas.getBoundingClientRect();
		return { x: evt.clientX - rect.left, y: evt.clientY - rect.top };
	}

    // runs game
    function run() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ball.update(canvas);
        //enemy.update();

        if(Rectangle.hasCollided(player.rectangle, ball.rectangle)
            //|| Rectangle.hasCollided(enemy.rectangle, ball.rectangle)
        ){
            ball.velX = -(ball.velX);
        }

        //RENDER - render the updated position of all the
        ball.draw(ctx);
        player.draw(ctx);
        //enemy.draw(ctx);

    }

    setInterval(run, 24);
}
