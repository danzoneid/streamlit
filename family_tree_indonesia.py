import streamlit as st
from collections import deque
import pandas as pd

# Struktur data keluarga dengan nama-nama Indonesia
family_tree = {
    'latif': ['sahuri'],
    'sahuri': ['marfuah', 'siti', 'slamet', 'soleh'],
    'marfuah': ['heli', 'santi', 'arik'],
    'siti': ['wawan', 'aldi'],
    'slamet': ['yusuf'],
    'soleh': ['jada', 'jihan'],
    'heli': [],
    'santi': [],
    'arik': [],
    'wawan': [],
    'aldi': [],
    'yusuf': [],
    'jada': [],
    'jihan': []
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
    st.title("Penelusuran Silsilah Keluarga Menggunakan BFS(Breadth Firs Search)")
    st.write("""
    Aplikasi ini disusun oleh kelompok 2 yang beranggotakan : Yusuf Danda Purwanto(32602200134), Heru Hidayatulloh(32602200075), M. Mifttahul Huda(32602200095), Franklyn Rama Fitrah A(32602200067)
    """)

    # Daftar semua anggota keluarga
    family_members = list(family_tree.keys())

    # Pilih anggota keluarga awal dan tujuan dari dropdown
    start_person = st.selectbox("Pilih nama awal (Initial Statement):", family_members)
    goal_person = st.selectbox("Pilih nama yang ingin dicari(goal statement):", family_members)

    # Tombol untuk memulai pencarian
    if st.button("Cari Jalur"):
        result, search_process = bfs(family_tree, start_person, goal_person)

        if result:
            # Menampilkan jalur yang ditemukan dengan lebih menarik
            st.success(f"Jalur ditemukan: {' -> '.join(result)}")
            st.balloons()  # Tambahkan efek balon untuk menambah interaksi
            st.write(f"Jalur dari **{start_person}** ke **{goal_person}**: ")
            st.markdown(f"<h2 style='text-align: center; color: green;'>{' -> '.join(result)}</h2>", unsafe_allow_html=True)
        else:
            st.error(f"{goal_person} tidak ditemukan dalam jalur keluarga dari {start_person}.")
        
        # Menampilkan proses pencarian dalam tabel dengan penjelasan di bawahnya
        if search_process:
            df = pd.DataFrame(search_process)
            st.write("### Proses Pencarian BFS:")
            st.table(df)
            

if __name__ == "__main__":
    main()
