function addDoctor() {
$(".error-message").text("");
$("input").removeClass("input-error");

let data={
name:$("#name").val().trim(),
specialty:$("#specialty").val().trim(),
conditions:$("#conditions").val().trim(),
experience:$("#experience").val().trim(),
education:$("#education").val().trim(),
insurance:$("#insurance").val().trim(),
location:$("#location").val().trim(),
phone:$("#phone").val().trim(),
image:$("#image").val()
}

let error=false

if(data.name===""){
$("#name_error").text("Name cannot be blank")
$("#name").addClass("input-error")
error=true
}

if(data.specialty===""){
$("#specialty_error").text("Specialty cannot be blank")
$("#specialty").addClass("input-error")
error=true
}

if(data.conditions===""){
$("#conditions_error").text("Conditions cannot be blank")
$("#conditions").addClass("input-error")
error=true
}

if(data.education===""){
$("#education_error").text("Education cannot be blank")
$("#education").addClass("input-error")
error=true
}

if(data.insurance===""){
$("#insurance_error").text("Insurance cannot be blank")
$("#insurance").addClass("input-error")
error=true
}

if(data.experience==="" || isNaN(data.experience)){
$("#experience_error").text("Experience must be numeric")
$("#experience").addClass("input-error")
error=true
}

if(data.phone==="" || isNaN(data.phone)){
$("#phone_error").text("Phone must be numeric")
$("#phone").addClass("input-error")
error=true
}

if(data.location===""){
$("#location_error").text("Location cannot be blank")
$("#location").addClass("input-error")
error=true
}

if(error){
return
}

$.ajax({
url:"/add_item",
type:"POST",
contentType:"application/json",
data:JSON.stringify(data),

success:function(response){

$("#success").show()

$("#success").html(
"New item successfully created. <a href='/view/"+response.id+"'>See it here</a>"
)

$("input").val("")
$("#name").focus()

}
})

}


function updateDoctor(){

let data={
id:$("#id").val(),
name:$("#name").val(),
specialty:$("#specialty").val(),
conditions:$("#conditions").val(),
experience:$("#experience").val(),
education:$("#education").val(),
insurance:$("#insurance").val(),
location:$("#location").val(),
phone:$("#phone").val(),
image:$("#image").val()
}

$.ajax({
url:"/update_item",
type:"POST",
contentType:"application/json",
data:JSON.stringify(data),

success:function(){
window.location="/view/"+$("#id").val()
}
})

}



function discard(){

if(confirm("Are you sure you want to discard changes?")){
window.history.back()
}

}



$(document).ready(function(){
$("#submitDoctor").click(function(){
addDoctor();
});
});
