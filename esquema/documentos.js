db.directores.insertMany([
{
    idDirector: 1,
    nombre: "Christopher",
    apellido: "Nolan",
    pais: "Reino Unido",
    fechaNacimiento: ISODate("1970-07-30"),
    premios: ["Oscar", "BAFTA"]
},
{
    idDirector: 2,
    nombre: "Steven",
    apellido: "Spielberg",
    pais: "Estados Unidos",
    fechaNacimiento: ISODate("1946-12-18"),
    premios: ["Oscar"]
},
{
    idDirector: 3,
    nombre: "Quentin",
    apellido: "Tarantino",
    pais: "Estados Unidos",
    fechaNacimiento: ISODate("1963-03-27"),
    premios: ["Oscar"]
},
{
    idDirector: 4,
    nombre: "Martin",
    apellido: "Scorsese",
    pais: "Estados Unidos",
    fechaNacimiento: ISODate("1942-11-17"),
    premios: ["Oscar"]
},
{
    idDirector: 5,
    nombre: "James",
    apellido: "Cameron",
    pais: "Canadá",
    fechaNacimiento: ISODate("1954-08-16"),
    premios: ["Oscar"]
},
{
    idDirector: 6,
    nombre: "Patty",
    apellido: "Jenkins",
    pais: "Estados Unidos",
    fechaNacimiento: ISODate("1971-07-24"),
    premios: []
},
{
    idDirector: 7,
    nombre: "Denis",
    apellido: "Villeneuve",
    pais: "Canadá",
    fechaNacimiento: ISODate("1967-10-03"),
    premios: []
},
{
    idDirector: 8,
    nombre: "Greta",
    apellido: "Gerwig",
    pais: "Estados Unidos",
    fechaNacimiento: ISODate("1983-08-04"),
    premios: []
},
{
    idDirector: 9,
    nombre: "Bong",
    apellido: "Joon-ho",
    pais: "Corea del Sur",
    fechaNacimiento: ISODate("1969-09-14"),
    premios: ["Oscar"]
},
{
    idDirector: 10,
    nombre: "Ridley",
    apellido: "Scott",
    pais: "Reino Unido",
    fechaNacimiento: ISODate("1937-11-30"),
    premios: []
}
]);

db.peliculas.insertMany([
{
idPelicula:101,
titulo:"Inception",
anioEstreno:2010,
genero:"Ciencia Ficción",
duracion:148,
idDirector:1,
idioma:"Inglés",
clasificacion:"PG-13",
paisProduccion:"Estados Unidos"
},
{
idPelicula:102,
titulo:"Interstellar",
anioEstreno:2014,
genero:"Ciencia Ficción",
duracion:169,
idDirector:1,
idioma:"Inglés",
clasificacion:"PG-13",
paisProduccion:"Estados Unidos"
},
{
idPelicula:103,
titulo:"Jurassic Park",
anioEstreno:1993,
genero:"Aventura",
duracion:127,
idDirector:2,
idioma:"Inglés",
clasificacion:"PG-13",
paisProduccion:"Estados Unidos"
},
{
idPelicula:104,
titulo:"Saving Private Ryan",
anioEstreno:1998,
genero:"Bélica",
duracion:169,
idDirector:2,
idioma:"Inglés",
clasificacion:"R",
paisProduccion:"Estados Unidos"
},
{
idPelicula:105,
titulo:"Pulp Fiction",
anioEstreno:1994,
genero:"Crimen",
duracion:154,
idDirector:3,
idioma:"Inglés",
clasificacion:"R",
paisProduccion:"Estados Unidos"
},
{
idPelicula:106,
titulo:"Kill Bill Vol. 1",
anioEstreno:2003,
genero:"Acción",
duracion:111,
idDirector:3,
idioma:"Inglés",
clasificacion:"R",
paisProduccion:"Estados Unidos"
},
{
idPelicula:107,
titulo:"The Departed",
anioEstreno:2006,
genero:"Drama",
duracion:151,
idDirector:4,
idioma:"Inglés",
clasificacion:"R",
paisProduccion:"Estados Unidos"
},
{
idPelicula:108,
titulo:"Avatar",
anioEstreno:2009,
genero:"Ciencia Ficción",
duracion:162,
idDirector:5,
idioma:"Inglés",
clasificacion:"PG-13",
paisProduccion:"Estados Unidos"
},
{
idPelicula:109,
titulo:"Titanic",
anioEstreno:1997,
genero:"Drama",
duracion:194,
idDirector:5,
idioma:"Inglés",
clasificacion:"PG-13",
paisProduccion:"Estados Unidos"
},
{
idPelicula:110,
titulo:"Wonder Woman",
anioEstreno:2017,
genero:"Acción",
duracion:141,
idDirector:6,
idioma:"Inglés",
clasificacion:"PG-13",
paisProduccion:"Estados Unidos"
},
{
idPelicula:111,
titulo:"Dune",
anioEstreno:2021,
genero:"Ciencia Ficción",
duracion:155,
idDirector:7,
idioma:"Inglés",
clasificacion:"PG-13",
paisProduccion:"Estados Unidos"
},
{
idPelicula:112,
titulo:"Arrival",
anioEstreno:2016,
genero:"Ciencia Ficción",
duracion:116,
idDirector:7,
idioma:"Inglés",
clasificacion:"PG-13",
paisProduccion:"Estados Unidos"
},
{
idPelicula:113,
titulo:"Barbie",
anioEstreno:2023,
genero:"Comedia",
duracion:114,
idDirector:8,
idioma:"Inglés",
clasificacion:"PG-13",
paisProduccion:"Estados Unidos"
},
{
idPelicula:114,
titulo:"Parasite",
anioEstreno:2019,
genero:"Drama",
duracion:132,
idDirector:9,
idioma:"Coreano",
clasificacion:"R",
paisProduccion:"Corea del Sur"
},
{
idPelicula:115,
titulo:"Gladiator",
anioEstreno:2000,
genero:"Acción",
duracion:155,
idDirector:10,
idioma:"Inglés",
clasificacion:"R",
paisProduccion:"Estados Unidos"
}
]);

db.resenas.insertMany([
{
idPelicula:101,
usuario:"ana23",
calificacion:5,
comentario:"Excelente película.",
fechaResena:ISODate("2024-01-15"),
utilidad:12
},
{
idPelicula:101,
usuario:"pedro89",
calificacion:4,
comentario:"Muy entretenida.",
fechaResena:ISODate("2024-03-20"),
utilidad:8
},
{
idPelicula:102,
usuario:"lucia77",
calificacion:5,
comentario:"Una obra maestra.",
fechaResena:ISODate("2024-04-10"),
utilidad:20
},
{
idPelicula:103,
usuario:"mario11",
calificacion:5,
comentario:"Un clásico.",
fechaResena:ISODate("2024-02-11"),
utilidad:14
},
{
idPelicula:104,
usuario:"sofia92",
calificacion:4,
comentario:"Muy emotiva.",
fechaResena:ISODate("2024-05-12"),
utilidad:5
},
{
idPelicula:105,
usuario:"juanp",
calificacion:5,
comentario:"Diálogos increíbles.",
fechaResena:ISODate("2024-06-02"),
utilidad:11
},
{
idPelicula:106,
usuario:"carla",
calificacion:4,
comentario:"Acción de principio a fin.",
fechaResena:ISODate("2024-06-18"),
utilidad:6
},
{
idPelicula:107,
usuario:"andres",
calificacion:5,
comentario:"Excelente actuación.",
fechaResena:ISODate("2024-07-01"),
utilidad:18
},
{
idPelicula:108,
usuario:"felipe",
calificacion:4,
comentario:"Visualmente impresionante.",
fechaResena:ISODate("2024-07-20"),
utilidad:9
},
{
idPelicula:109,
usuario:"camila",
calificacion:5,
comentario:"Siempre emociona.",
fechaResena:ISODate("2024-08-11"),
utilidad:13
},
{
idPelicula:110,
usuario:"daniel",
calificacion:3,
comentario:"Buena pero esperaba más.",
fechaResena:ISODate("2024-09-04"),
utilidad:3
},
{
idPelicula:111,
usuario:"jose",
calificacion:5,
comentario:"Excelente adaptación.",
fechaResena:ISODate("2024-10-16"),
utilidad:17
},
{
idPelicula:112,
usuario:"fernanda",
calificacion:4,
comentario:"Muy interesante.",
fechaResena:ISODate("2024-11-08"),
utilidad:7
},
{
idPelicula:113,
usuario:"valentina",
calificacion:4,
comentario:"Muy divertida.",
fechaResena:ISODate("2025-01-10"),
utilidad:4
},
{
idPelicula:114,
usuario:"roberto",
calificacion:5,
comentario:"Una crítica social brillante.",
fechaResena:ISODate("2025-02-12"),
utilidad:16
},
{
idPelicula:115,
usuario:"marcela",
calificacion:5,
comentario:"Una película épica.",
fechaResena:ISODate("2025-03-14"),
utilidad:15
}
]);