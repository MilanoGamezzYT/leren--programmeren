function bereken_poten() {
    const aantal_giraffen = parseInt(document.getElementById("aantal-giraffen").value);
    const aantal_struisvogels = parseInt(document.getElementById("aantal-struisvogels").value);
    const aantal_zebras = parseInt(document.getElementById("aantal-zebras").value);
  
    const poten_giraffen = aantal_giraffen * 4;
    const poten_struisvogels = aantal_struisvogels * 2;
    const poten_zebras = aantal_zebras * 4;
    const totaal_poten = poten_giraffen + poten_struisvogels + poten_zebras;
  
    document.getElementById("resultaat").innerHTML = "Het totale aantal poten is: " + totaal_poten;
  }
  