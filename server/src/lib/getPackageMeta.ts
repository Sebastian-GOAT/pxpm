import { collection, query, where, getDocs } from 'firebase/firestore';
import { db } from './firebase.ts';
import type { PackageMeta } from '../types/PackageMeta.ts';

export interface Data extends PackageMeta {
    id: string;
}

export default async function getPackageMeta(name: string): Promise<Data | null> {

    const q = query(collection(db, 'packages'), where('name', '==', name));

    const querySnapshot = await getDocs(q);
    if (querySnapshot.empty) return null;

    const doc = querySnapshot.docs[0];
    if (!doc) return null;

    return {
        id: doc.id,
        ...(doc.data() as PackageMeta)
    };
}