/*
How to Execute:
1. Open terminal in this project folder.
2. Run: npx expo start
3. Press 'w' for Web or 'a' for Emulator.
*/
import React from 'react';
import { View, Text, FlatList, StyleSheet } from 'react-native';

const items = [
  { id: '1', name: 'Fresh Milk', price: '$3.50', img: '🥛' },
  { id: '2', name: 'Organic Bread', price: '$2.00', img: '🍞' },
  { id: '3', name: 'Farm Eggs', price: '$4.99', img: '🥚' },
];

export default function App() {
  return (
    <View style={styles.container}>
      <Text style={styles.header}>Walmart Grocery</Text>
      <FlatList data={items} keyExtractor={item => item.id} renderItem={({ item }) => (
        <View style={styles.item}>
            <Text style={{fontSize: 30}}>{item.img}</Text>
            <View>
                <Text style={styles.name}>{item.name}</Text>
                <Text style={styles.price}>{item.price}</Text>
            </View>
        </View>
      )} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, padding: 50, backgroundColor: '#0071ce' },
  header: { fontSize: 24, fontWeight: 'bold', color: 'white', marginBottom: 20 },
  item: { backgroundColor: 'white', padding: 15, borderRadius: 10, marginBottom: 10, flexDirection: 'row', gap: 20, alignItems: 'center' },
  name: { fontWeight: 'bold', fontSize: 16 },
  price: { color: 'green' }
});