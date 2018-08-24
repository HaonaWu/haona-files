class Rectangle{

    constructor(x, y, width, height){
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }

    static hasCollided(rect1, rect2){
        if(rect1.x < rect2.x + rect2.width && 
            rect1.x + rect1.width > rect2.x && 
            rect1.y < rect2.y + rect2.height && 
            rect1.height + rect1.y > rect2.y){
                return true;
        }

        return false;
    }
}