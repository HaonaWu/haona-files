class Player{
    constructor(x, y, width, height){
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;

        this.color = "#F0F0F0"
        this.rectangle = new Rectangle(this.x, this.y, this.width, this.height);
    }

    draw(ctx){
        ctx.beginPath();
        ctx.fillStyle = this.color;
        ctx.fillRect(this.x, this.y, this.width, this.height);
        ctx.fill();
        ctx.closePath();
    }

    update(y){
        this.y = y - this.height/2;
        this.rectangle.x = this.x;
        this.rectangle.y = this.y;
    }
}
