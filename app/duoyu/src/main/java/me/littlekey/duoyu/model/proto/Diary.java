// Code generated by Wire protocol buffer compiler, do not edit.
// Source file: model/model.proto at 49:1
package me.littlekey.duoyu.model.proto;

import com.squareup.wire.FieldEncoding;
import com.squareup.wire.Message;
import com.squareup.wire.ProtoAdapter;
import com.squareup.wire.ProtoReader;
import com.squareup.wire.ProtoWriter;
import com.squareup.wire.WireField;
import com.squareup.wire.internal.Internal;
import java.io.IOException;
import java.lang.Integer;
import java.lang.Object;
import java.lang.Override;
import java.lang.String;
import java.lang.StringBuilder;
import okio.ByteString;

public final class Diary extends Message<Diary, Diary.Builder> {
  public static final ProtoAdapter<Diary> ADAPTER = new ProtoAdapter_Diary();

  private static final long serialVersionUID = 0L;

  public static final String DEFAULT_DIARY_ID = "";

  public static final String DEFAULT_TITLE = "";

  public static final Language DEFAULT_LANGUAGE = Language.CHINESE;

  public static final String DEFAULT_CONTENT = "";

  public static final Integer DEFAULT_DATE = 0;

  @WireField(
      tag = 1,
      adapter = "com.squareup.wire.ProtoAdapter#STRING"
  )
  public final String diary_id;

  @WireField(
      tag = 2,
      adapter = "com.squareup.wire.ProtoAdapter#STRING"
  )
  public final String title;

  @WireField(
      tag = 3,
      adapter = "me.littlekey.duoyu.model.proto.User#ADAPTER"
  )
  public final User author;

  @WireField(
      tag = 4,
      adapter = "me.littlekey.duoyu.model.proto.Language#ADAPTER"
  )
  public final Language language;

  @WireField(
      tag = 5,
      adapter = "com.squareup.wire.ProtoAdapter#STRING"
  )
  public final String content;

  @WireField(
      tag = 6,
      adapter = "com.squareup.wire.ProtoAdapter#INT32"
  )
  public final Integer date;

  public Diary(String diary_id, String title, User author, Language language, String content, Integer date) {
    this(diary_id, title, author, language, content, date, ByteString.EMPTY);
  }

  public Diary(String diary_id, String title, User author, Language language, String content, Integer date, ByteString unknownFields) {
    super(ADAPTER, unknownFields);
    this.diary_id = diary_id;
    this.title = title;
    this.author = author;
    this.language = language;
    this.content = content;
    this.date = date;
  }

  @Override
  public Builder newBuilder() {
    Builder builder = new Builder();
    builder.diary_id = diary_id;
    builder.title = title;
    builder.author = author;
    builder.language = language;
    builder.content = content;
    builder.date = date;
    builder.addUnknownFields(unknownFields());
    return builder;
  }

  @Override
  public boolean equals(Object other) {
    if (other == this) return true;
    if (!(other instanceof Diary)) return false;
    Diary o = (Diary) other;
    return unknownFields().equals(o.unknownFields())
        && Internal.equals(diary_id, o.diary_id)
        && Internal.equals(title, o.title)
        && Internal.equals(author, o.author)
        && Internal.equals(language, o.language)
        && Internal.equals(content, o.content)
        && Internal.equals(date, o.date);
  }

  @Override
  public int hashCode() {
    int result = super.hashCode;
    if (result == 0) {
      result = unknownFields().hashCode();
      result = result * 37 + (diary_id != null ? diary_id.hashCode() : 0);
      result = result * 37 + (title != null ? title.hashCode() : 0);
      result = result * 37 + (author != null ? author.hashCode() : 0);
      result = result * 37 + (language != null ? language.hashCode() : 0);
      result = result * 37 + (content != null ? content.hashCode() : 0);
      result = result * 37 + (date != null ? date.hashCode() : 0);
      super.hashCode = result;
    }
    return result;
  }

  @Override
  public String toString() {
    StringBuilder builder = new StringBuilder();
    if (diary_id != null) builder.append(", diary_id=").append(diary_id);
    if (title != null) builder.append(", title=").append(title);
    if (author != null) builder.append(", author=").append(author);
    if (language != null) builder.append(", language=").append(language);
    if (content != null) builder.append(", content=").append(content);
    if (date != null) builder.append(", date=").append(date);
    return builder.replace(0, 2, "Diary{").append('}').toString();
  }

  public static final class Builder extends Message.Builder<Diary, Builder> {
    public String diary_id;

    public String title;

    public User author;

    public Language language;

    public String content;

    public Integer date;

    public Builder() {
    }

    public Builder diary_id(String diary_id) {
      this.diary_id = diary_id;
      return this;
    }

    public Builder title(String title) {
      this.title = title;
      return this;
    }

    public Builder author(User author) {
      this.author = author;
      return this;
    }

    public Builder language(Language language) {
      this.language = language;
      return this;
    }

    public Builder content(String content) {
      this.content = content;
      return this;
    }

    public Builder date(Integer date) {
      this.date = date;
      return this;
    }

    @Override
    public Diary build() {
      return new Diary(diary_id, title, author, language, content, date, super.buildUnknownFields());
    }
  }

  private static final class ProtoAdapter_Diary extends ProtoAdapter<Diary> {
    ProtoAdapter_Diary() {
      super(FieldEncoding.LENGTH_DELIMITED, Diary.class);
    }

    @Override
    public int encodedSize(Diary value) {
      return (value.diary_id != null ? ProtoAdapter.STRING.encodedSizeWithTag(1, value.diary_id) : 0)
          + (value.title != null ? ProtoAdapter.STRING.encodedSizeWithTag(2, value.title) : 0)
          + (value.author != null ? User.ADAPTER.encodedSizeWithTag(3, value.author) : 0)
          + (value.language != null ? Language.ADAPTER.encodedSizeWithTag(4, value.language) : 0)
          + (value.content != null ? ProtoAdapter.STRING.encodedSizeWithTag(5, value.content) : 0)
          + (value.date != null ? ProtoAdapter.INT32.encodedSizeWithTag(6, value.date) : 0)
          + value.unknownFields().size();
    }

    @Override
    public void encode(ProtoWriter writer, Diary value) throws IOException {
      if (value.diary_id != null) ProtoAdapter.STRING.encodeWithTag(writer, 1, value.diary_id);
      if (value.title != null) ProtoAdapter.STRING.encodeWithTag(writer, 2, value.title);
      if (value.author != null) User.ADAPTER.encodeWithTag(writer, 3, value.author);
      if (value.language != null) Language.ADAPTER.encodeWithTag(writer, 4, value.language);
      if (value.content != null) ProtoAdapter.STRING.encodeWithTag(writer, 5, value.content);
      if (value.date != null) ProtoAdapter.INT32.encodeWithTag(writer, 6, value.date);
      writer.writeBytes(value.unknownFields());
    }

    @Override
    public Diary decode(ProtoReader reader) throws IOException {
      Builder builder = new Builder();
      long token = reader.beginMessage();
      for (int tag; (tag = reader.nextTag()) != -1;) {
        switch (tag) {
          case 1: builder.diary_id(ProtoAdapter.STRING.decode(reader)); break;
          case 2: builder.title(ProtoAdapter.STRING.decode(reader)); break;
          case 3: builder.author(User.ADAPTER.decode(reader)); break;
          case 4: {
            try {
              builder.language(Language.ADAPTER.decode(reader));
            } catch (ProtoAdapter.EnumConstantNotFoundException e) {
              builder.addUnknownField(tag, FieldEncoding.VARINT, (long) e.value);
            }
            break;
          }
          case 5: builder.content(ProtoAdapter.STRING.decode(reader)); break;
          case 6: builder.date(ProtoAdapter.INT32.decode(reader)); break;
          default: {
            FieldEncoding fieldEncoding = reader.peekFieldEncoding();
            Object value = fieldEncoding.rawProtoAdapter().decode(reader);
            builder.addUnknownField(tag, fieldEncoding, value);
          }
        }
      }
      reader.endMessage(token);
      return builder.build();
    }

    @Override
    public Diary redact(Diary value) {
      Builder builder = value.newBuilder();
      if (builder.author != null) builder.author = User.ADAPTER.redact(builder.author);
      builder.clearUnknownFields();
      return builder.build();
    }
  }
}
