import streamlit as st
from collections import deque
import pandas as pd

# Struktur data keluarga dengan nama-nama Indonesia
family_tree = {
    'Budi': ['Andi', 'Siti'],
    'Andi': ['Rina', 'Faisal'],
    'Siti': ['Dewi', 'Ridwan'],
    'Rina': ['Toni', 'Maya'],
    'Faisal': ['Agus', 'Putri'],
    'Dewi': ['Wawan', 'Fitria'],
    'Ridwan': ['Roni', 'Dian'],
    'Toni': [],
    'Maya': ['Bayu'],
    'Agus': [],
    'Putri': ['Lina'],
    'Wawan': ['Yuni'],
    'Fitria': [],
    'Roni': ['Siska'],
    'Dian': [],
    'Bayu': [],
    'Lina': [],
    'Yuni': [],
    'Siska': []
}

# Fungsi BFS untuk menelusuri graf keluarga dan menampilkan proses
def bfs(family_tree, start, goal):
    # Menggunakan deque sebagai queue untuk BFS
    queue = deque([(start, [start])])  # Queue menyimpan tuple (current_node, path)
    visited = set()  # Set untuk melacak node yang sudah dikunjungi
    search_process = []  # Untuk menyimpan proses pencarian
    
    while queue:
        vertex, path = queue.popleft()  # Ambil node terdepan dari queue
        visited.add(vertex)
        
        # Simpan proses ke tabel
        search_process.append({"Current Node": vertex, "Path": ' -> '.join(path)})
        
        if vertex == goal:
            return path, search_process
        
        for neighbor in family_tree.get(vertex, []):
            if neighbor not in visited and neighbor not in [n[0] for n in queue]:
                queue.append((neighbor, path + [neighbor]))
    
    return None, search_process  # Kembalikan None jika jalur tidak ditemukan

# Fungsi utama Streamlit untuk membangun UI
def main():
    st.title("Penelusuran Silsilah Keluarga Indonesia (BFS)")
    st.write("""
    Aplikasi ini memungkinkan Anda menelusuri silsilah keluarga dengan pencarian buta (Blind Search)
    menggunakan algoritma Breadth First Search (BFS). Proses pencarian juga akan ditampilkan secara visual dalam tabel.
    """)

    # Daftar semua anggota keluarga
    family_members = list(family_tree.keys())

    # Pilih anggota keluarga awal dan tujuan dari dropdown
    start_person = st.selectbox("Pilih nama awal (root):", family_members)
    goal_person = st.selectbox("Pilih nama yang ingin dicari:", family_members)

    # Tombol untuk memulai pencarian
    if st.button("Cari Jalur"):
        result, search_process = bfs(family_tree, start_person, goal_person)

        if result:
            st.success(f"Jalur ditemukan: {' -> '.join(result)}")
        else:
            st.error(f"{goal_person} tidak ditemukan dalam jalur keluarga dari {start_person}.")
        
        # Menampilkan proses pencarian dalam tabel
        if search_process:
            df = pd.DataFrame(search_process)
            st.write("Proses Pencarian BFS:")
            st.table(df)
        else:
            st.warning("Tidak ada proses pencarian yang dilakukan.")

if __name__ == "__main__":
    main()
