var student = {
    firstName: "Maya",
    course: "Full Stack Development", 
    learningTopics: ["objects", "functions", "this"],
    completedLessons: 3,
    totalLessons: 5,


getProgressMessage : function(){
    var percentage = (this.completedLessons / this.totalLessons)* 100;
    return this.firstName + " finished " + percentage + "% of the lessons.";
    
    }
};

function printMessage(message) {
console.log( "MESSAGE: " + message.toUpperCase());
}


//console.log(getLearningPlan(trainee));

printMessage(student.getProgressMessage(student));

const progressMessage = student.getProgressMessage.bind(student);
console.log(progressMessage());