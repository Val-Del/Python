const requ = new XMLHttpRequest();
let input = document.querySelector('.flex .inputAPI');
let submit = document.querySelector('.flex .btnAPI');
let repAPI =  document.querySelector('.flex .repAPI');
// console.log(submit)
let request;
let namePokemon;
let back;
submit.addEventListener('click', function(){
    // console.log(input)
    // console.log(input.value)

  
    namePokemon = input.value.toLowerCase();
    request = "https://pokeapi.co/api/v2/pokemon/" + namePokemon
      /**** GET by nom  */
      requ.open('GET', request, true);
      //requ.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
     requ.send();
})

requ.onreadystatechange = function(event) {
    if (this.readyState === XMLHttpRequest.DONE) {
        if (this.status === 200) {
            // console.log("Réponse reçue: %s", this.responseText);;
            //console.log(this.responseText);
           // reponse=JSON.parse(this.responseText);
          //  repAPI.innerHTML = this.responseText;
         
          reponse=JSON.parse(this.responseText);
          repAPI.innerHTML = reponse.types[0].type.name;
        //   console.log(types[0].type.name);
          console.log(reponse)


         
            
        } else {
            console.log("Status de la réponse: %d (%s)", this.status, this.statusText);
        }
    }
};