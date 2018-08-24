class Ball{
    constructor(x, y, radius){
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.color = "#F0F0F0"

        this.velX = 8;
        this.velY = 8;
        this.rectangle = new Rectangle(this.x, this.y, this.radius, this.radius);
    }

    draw(ctx){
        ctx.beginPath();
        ctx.fillStyle = this.color;
        ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
        ctx.fill();
        ctx.closePath();
    }

    update(canvas){
        // update the x and y value of the ball
        this.x += this.velX;
        this.y += this.velY;
        this.rectangle.x = this.x;
        this.rectangle.y = this.y;

        // if the ball collides with either left or right wall, reflect the ball
        if(this.x <= 0 || this.x >= canvas.width-this.radius){
            this.velX = -(this.velX);
        }

        // if the ball collides with either top or bottom wall, reflect the ball
        if(this.y <= 0 || this.y >= canvas.height - this.radius){
            this.velY = -(this.velY);
        }
    }
}
