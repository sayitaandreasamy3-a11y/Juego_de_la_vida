
import streamlit as st
import numpy as np
import time

st.set_page_config(
    page_title="Juego de la Vida",
    page_icon="🧬",
    layout="wide"
)

ANCHO = 800
ALTO = 600
TAM_CELDA = 10

ROWS = ALTO // TAM_CELDA
COLS = ANCHO // TAM_CELDA

st.title("🧬 Juego de la Vida")
st.write("Simulación del autómata celular de Conway")

# Crear el tablero inicial
if "board" not in st.session_state:
    st.session_state.board = np.zeros(
        (ROWS, COLS), dtype=int
    )

if "generacion" not in st.session_state:
    st.session_state.generacion = 0


# Actualizar las células
def actualizar_board(board):
    new_board = board.copy()

    for row in range(ROWS):
        for col in range(COLS):

            inicio_fila = max(0, row - 1)
            fin_fila = min(ROWS, row + 2)
            inicio_col = max(0, col - 1)
            fin_col = min(COLS, col + 2)

            vecinos = np.sum(
                board[inicio_fila:fin_fila,
                      inicio_col:fin_col]
            ) - board[row, col]

            if board[row, col] == 1:
                if vecinos < 2 or vecinos > 3:
                    new_board[row, col] = 0

            elif vecinos == 3:
                new_board[row, col] = 1

    return new_board


# Dibujar el tablero
def mostrar_board(board):
    imagen = np.zeros((ROWS, COLS, 3), dtype=np.uint8)

    imagen[board == 1] = [225, 255, 255]

    st.image(
        imagen,
        caption="Tablero del Juego de la Vida",
        width=800
    )


# Información
st.subheader(
    f"Generación actual: {st.session_state.generacion}"
)

# Botones
col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("🎲 Aleatorio"):
        st.session_state.board = np.random.choice(
            [0, 1],
            size=(ROWS, COLS),
            p=[0.8, 0.2]
        )
        st.session_state.generacion = 0
        st.rerun()

with col2:
    if st.button("▶ Siguiente generación"):
        st.session_state.board = actualizar_board(
            st.session_state.board
        )
        st.session_state.generacion += 1
        st.rerun()

with col3:
    if st.button("⏩ Ejecutar 30 generaciones"):
        imagen = st.empty()

        for i in range(30):
            st.session_state.board = actualizar_board(
                st.session_state.board
            )
            st.session_state.generacion += 1

            board = st.session_state.board

            pixels = np.zeros((ROWS, COLS, 3), dtype=np.uint8)
            pixels[board == 1] = [225, 255, 255]

            imagen.image(pixels, width=800)
            time.sleep(0.15)

        st.rerun()

with col4:
    if st.button("🗑 Limpiar"):
        st.session_state.board = np.zeros(
            (ROWS, COLS), dtype=int
        )
        st.session_state.generacion = 0
        st.rerun()


# Mostrar tablero
mostrar_board(st.session_state.board)

st.divider()

st.markdown("""
### ¿Cómo funciona?

- **Aleatorio:** crea células en posiciones aleatorias.
- **Siguiente generación:** avanza una generación.
- **Ejecutar 30 generaciones:** reproduce 30 generaciones.
- **Limpiar:** elimina todas las células.

### Reglas del Juego de la Vida

1. Una célula con menos de dos vecinos vivos muere.
2. Una célula con dos o tres vecinos sobrevive.
3. Una célula con más de tres vecinos muere.
4. Una célula muerta con exactamente tres vecinos revive.
""")
