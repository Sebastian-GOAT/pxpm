import { collection, query, where, getDocs } from 'firebase/firestore';
import type { Data } from './getPackageMeta.ts';
import { db } from './firebase.ts';
import { PackageMeta } from '../types/PackageMeta.ts';

interface Options {
    limit: number;
    skip: number;
    query: string;
    keywords: string[];
}

export default async function getPackages(options: Options): Promise<Data[]> {

    const searchQuery = options.query;

    const end = searchQuery.slice(0, -1) + String.fromCharCode(searchQuery.charCodeAt(searchQuery.length - 1) + 1);

    const conditions: any[] = [
        where('name', '>=', searchQuery),
        where('name', '<=', end),
    ];

    if (options.keywords.length > 0)
        conditions.push(where('keywords', 'array-contains-any', options.keywords));

    const q = query(
        collection(db, 'packages'),
        ...conditions
    );

    const snapshot = await getDocs(q);
    if (snapshot.empty) return [];

    const docs = snapshot.docs.map(doc => ({
        id: doc.id,
        ...(doc.data() as PackageMeta)
    }));

    return docs.slice(options.skip, options.skip + options.limit);
}