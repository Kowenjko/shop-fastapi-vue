export const handleImageError = (event: Event, size = '400x400') => {
  const img = event.target as HTMLImageElement
  img.src = `https://via.placeholder.com/${size}?text=No+Image`
}
