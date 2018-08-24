class Enemy{
    constructor(x, y, width, height, ball){
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
        this.ball = ball;
        
        this.rectangle = new Rectangle(this.x, this.y, this.width, this.height);
        this.color = "#F0F0F0"
    }

    draw(ctx){
        ctx.beginPath();
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x, this.y, this.width, this.height);
        ctx.fill();
        ctx.closePath();
    }

    update(){
        this.y = this.ball.y - this.height/2;
        this.rectangle.x = this.x;
        this.rectangle.y = this.y;
    }
}