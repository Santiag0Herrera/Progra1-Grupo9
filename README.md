# 🗳️ **Simulación de Resultados Electorales** 

## Descripción del Proyecto

Este proyecto simula resultados electorales basados en la población total y el número de provincias. Utiliza datos simulados generados con la biblioteca `random` para representar votos de diferentes candidatos, cada uno asociado a un partido único. Se ofrecen informes detallados de porcentajes de votos y condiciones para una posible segunda vuelta (balotaje).

---

## 🚀 **Requisitos y Alcance del Proyecto**

### 1. Entrada de Datos:
   - El programa recibe como entrada **dos parámetros**:
     - La población total de votantes.
     - La cantidad de provincias.

### 2. Generación de Datos Simulados:
   - Se utiliza la biblioteca `random` para generar votos simulados, respetando la tendencia de voto de cada candidato.
   - **Reglas**:
     - Cada candidato está asociado a un único partido.
     - Los datos simulados deben reflejar diferentes escenarios electorales.

### 3. Informes y Salidas:
   - El programa genera y presenta los siguientes informes:
     - **Porcentajes de intención de voto** para cada candidato y partido.
     - Condiciones y fórmulas para determinar si es necesaria una **segunda vuelta (balotaje)**.
     - **Tendencias electorales** observadas a lo largo del tiempo (si aplica).

### Recomendaciones de la Profesora:
   - Preinicializar provincias, población por provincias, población y candidatos.
   - Ingresar, mediante un menú de navegación, las opciones para visualizar los informes.
   - Usar un **multiplicador de 0 a 5** para los votos generados de forma aleatoria.
   - Validar que el multiplicador no haga que los votos totales excedan la población.

---

## 🛠️ **Organización del Proyecto**

### **1. Entrada de Datos y Validaciones** 
- Desarrollador 1:
  - Implementación de la función `ingresar_datos()`.
  - Validación de los datos ingresados (población > 0, número de provincias válido).
  
### **2. Preinicialización de Provincias y Candidatos**
- Desarrollador 2:
  - Crear la lista de provincias y dividir la población proporcionalmente.
  - Definir candidatos y sus partidos.

### **3. Generación de Datos Simulados**
- Desarrollador 3:
  - Usar `random` para generar votos, respetando el multiplicador (0-5).
  - Evitar que los votos superen la población total.

### **4. Cálculo de Porcentajes y Segunda Vuelta**
- Desarrollador 4:
  - Calcular los porcentajes de votos obtenidos.
  - Verificar condiciones para balotaje (segunda vuelta).

### **5. Informes, Menú y Tendencias**
- Desarrollador 5:
  - Implementar el menú de navegación para acceder a los informes.
  - Crear los informes visualizando los porcentajes y las tendencias electorales.

---

## 🧑‍💻 **Equipo de Desarrollo**

- **Santiago Albuixech**: [Nombre del dev 1] - _Entrada de datos y validaciones_
- **Francisco Berdezagar**: [Nombre del dev 2] - _Preinicialización de provincias y candidatos_
- **Santiago Herrera**: [Nombre del dev 3] - _Generación de datos simulados_
- **Nicolas Villreal**: [Nombre del dev 4] - _Cálculo de porcentajes y segunda vuelta_
- **Matí as Ortiz**: [Nombre del dev 5] - _Informes, menú y tendencias_

---

## 📈 **Instrucciones para ejecutar el proyecto**:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-repo/simulacion-electoral.git