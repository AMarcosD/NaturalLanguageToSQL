### Desafio Sofia Salud
![](DesafioSofia.drawio.png)

En este desafío, se desarrollo una solución que satisface la necesidad de consultar con lenguaje natural a un asistente impulsado por LLM (**Gemini**) con el objetivo de obtener una Query compatible con el principal dispositivo de almacenamiento (**PostgreSQL**).  
Se decidió utilizar **LangChain** para generar eficiencia en cada prompt enviado por el usuario.  
Se solicitó el uso de DBT para el procesamiento de los datos almacenados en PostgreSQL.  

En el mismo, se decidió separar el uso en dos entornos. Uno dedicado a DBT y otro a el LLM por conflicto entre dependencias del primero y Gemini.
Por otro lado, se decidió alimentar el agente con un resumen generado a partir de un script que consume el schema.yml del proyecto DBT para eficientizar el uso de tokens y descartanto por el mismo motivo la consideración del manifest de DBT.  

A continuación, podrán encontrar el manual de uso para los usuarios que quieran adoptar la solución.  
[How to Use - StakeHolders Documentation](HowToUse.md)
