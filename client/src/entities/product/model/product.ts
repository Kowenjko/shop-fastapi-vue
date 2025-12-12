export interface ProductI {
  id: number
  name: string
  description: string
  price: number
  category_id: number
  image_url: string
  created_at: string
  category: {
    name: string
    slug: string
    id: number
  }
}

export interface CreateProductI {
  name: string
  description: string
  price: number
  category_id: number
  image_url: string
}

export interface AllProductI {
  products: ProductI[]
  total: number
}
