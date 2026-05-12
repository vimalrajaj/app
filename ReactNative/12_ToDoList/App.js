/*
How to Execute:
1. Open terminal in this project folder.
2. Run: npx expo start
3. Press 'w' for Web or 'a' for Emulator.
*/
import React, { useState } from 'react';
import { View, TextInput, Button, FlatList, Text, StyleSheet } from 'react-native';

export default function App() {
  const [task, setTask] = useState('');
  const [tasks, setTasks] = useState([]);

  return (
    <View style={styles.container}>
        <Text style={styles.title}>Daily To-Dos</Text>
        <TextInput placeholder="New Task" value={task} onChangeText={setTask} style={styles.input} />
        <Button title="Add Task" onPress={() => { if(task){ setTasks([{task, id: Date.now().toString()}, ...tasks]); setTask(''); } }} />
        <FlatList data={tasks} keyExtractor={item => item.id} renderItem={({item}) => (
            <Text style={styles.item}>• {item.task}</Text>
        )} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { padding: 50, flex: 1 },
  title: { fontSize: 22, fontWeight: 'bold', marginBottom: 20 },
  input: { borderBottomWidth: 1, marginBottom: 15, padding: 8 },
  item: { fontSize: 18, marginTop: 10 }
});